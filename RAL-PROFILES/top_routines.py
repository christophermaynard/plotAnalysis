#!/usr/bin/env python3
"""Strong-scaling table for the most expensive Vernier callipers.

Ranks routines by self time at the baseline decomposition and tabulates that
self time across every decomposition. Self time is used because Vernier
callipers nest, so total times double-count up the tree.

Usage:
    python top_routines.py run1/summaries/vernier_long.csv \
                           run3/summaries/vernier_long.csv
"""

import argparse
from pathlib import Path

import pandas as pd

METRIC = "Self Max(s)"


def load(paths, metric=METRIC):
    frames = [pd.read_csv(p) for p in paths]
    df = pd.concat(frames, ignore_index=True)
    order = (df[["decomposition", "cores", "threads"]].drop_duplicates()
             .sort_values(["cores", "threads"])["decomposition"].tolist())
    # Several runs of the same decomposition: keep the fastest.
    best = df.groupby(["decomposition", "routine"], as_index=False)[metric].min()
    return best, order


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, nargs="+")
    parser.add_argument("-n", "--top", type=int, default=10)
    parser.add_argument("--baseline",
                        help="Decomposition to rank by (default: fewest cores, 1T).")
    parser.add_argument("--metric", default=METRIC)
    parser.add_argument("--speedup", action="store_true",
                        help="Add a baseline/fastest speedup column.")
    args = parser.parse_args()

    df, order = load(args.csv, args.metric)
    table = df.pivot(index="routine", columns="decomposition", values=args.metric)[order]
    args.baseline = args.baseline or order[0]

    ranked = table.sort_values(args.baseline, ascending=False).head(args.top)

    if args.speedup:
        ranked = ranked.assign(speedup=ranked[args.baseline] / ranked.min(axis=1))

    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 50)
    print(ranked.round(2).to_string())


if __name__ == "__main__":
    main()
