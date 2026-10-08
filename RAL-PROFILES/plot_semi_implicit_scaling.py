#!/usr/bin/env python3
"""Strong scaling of semi_implicit_timestep against node count."""

import argparse
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FixedLocator, FuncFormatter

ROUTINE = "semi_implicit_timestep"
METRIC = "Total Max(s)"
CORES_PER_NODE = 192  # Genoa


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, nargs="+",
                        help="One or more vernier_long.csv files. Where a "
                             "decomposition appears in several, the fastest "
                             "time is kept.")
    parser.add_argument("-o", "--output", type=Path,
                        default=Path("semi_implicit_scaling.png"))
    parser.add_argument("--anchor", default="24x24_1T",
                        help="Decomposition the ideal scaling line passes "
                             "through.")
    args = parser.parse_args()

    df = pd.concat([pd.read_csv(p).assign(run=p.parent.parent.name)
                    for p in args.csv], ignore_index=True)
    sit = df[df["routine"] == ROUTINE]

    # Repeat runs of the same decomposition differ only by machine noise, so
    # the shortest time is the one least contaminated by it.
    sit = (sit.loc[sit.groupby("decomposition")[METRIC].idxmin()]
              .sort_values("cores"))
    for _, row in sit.iterrows():
        print(f"{row['decomposition']:10} {row[METRIC]:8.1f} s  ({row['run']})")

    # Kept fractional: the shortfall below the next integer is the idle part
    # of the tail node.
    sit = sit.assign(nodes=sit["cores"] / CORES_PER_NODE)

    threads = sorted(sit["threads"].unique())
    colours = plt.get_cmap("viridis")(np.linspace(0.15, 0.8, len(threads)))
    markers = ["o", "s", "^", "D"]

    fig, ax = plt.subplots(figsize=(10, 6.5))

    # Nodes actually allocated by the scheduler, so the gap to each data point
    # shows how much of the tail node is wasted.
    for i, nodes in enumerate(sorted(sit["nodes"].unique())):
        ax.axvline(math.ceil(nodes), color="firebrick", linestyle="-",
                   linewidth=0.9, alpha=0.5, zorder=0,
                   label="nodes allocated" if i == 0 else None)

    # Ideal scaling through the anchor decomposition, but placed at the whole
    # nodes it is charged for rather than the fraction it fills.
    match = sit[sit["decomposition"] == args.anchor]
    if match.empty:
        raise SystemExit(f"Anchor '{args.anchor}' not in {args.csv}")
    base_row = match.iloc[0]
    anchor_nodes = math.ceil(base_row["nodes"])
    nodes_ref = np.array([sit["nodes"].min(), sit["nodes"].max()], dtype=float)
    ax.plot(nodes_ref, base_row[METRIC] * anchor_nodes / nodes_ref,
            color="0.4", linestyle="--", linewidth=1.2, zorder=1,
            label=f"ideal through {args.anchor} at {anchor_nodes} nodes")
    ax.plot(anchor_nodes, base_row[METRIC], marker="*", markersize=16,
            color="0.4", markeredgecolor="black", markeredgewidth=0.5,
            linestyle="none", zorder=2)

    for i, nthreads in enumerate(threads):
        sub = sit[sit["threads"] == nthreads]
        ax.plot(sub["nodes"], sub[METRIC], marker=markers[i % len(markers)],
                color=colours[i], markersize=7, markeredgecolor="black",
                markeredgewidth=0.5, linewidth=1.6, zorder=3,
                label=f"{nthreads} thread{'s' if nthreads > 1 else ''}")

        for _, row in sub.iterrows():
            ax.annotate(f"{row['local_nx']}x{row['local_ny']}",
                        (row["nodes"], row[METRIC]),
                        textcoords="offset points", xytext=(6, -11),
                        fontsize=7, color="0.3")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ticks = sorted(sit["nodes"].unique())
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_minor_locator(FixedLocator([]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.2f}"))
    ax.yaxis.set_major_locator(FixedLocator([50, 100, 200, 400, 800]))
    ax.yaxis.set_minor_locator(FixedLocator([]))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))

    ax.set_xlabel(f"Nodes (cores / {CORES_PER_NODE}), fractional")
    ax.set_ylabel(f"{ROUTINE} {METRIC}, best of {len(args.csv)} run"
                  f"{'s' if len(args.csv) > 1 else ''}")
    ax.set_title("RAL3 672x672 UK strong scaling on EX1A\n"
                 "labels give the local volume per rank; red lines are whole "
                 "nodes allocated")
    ax.legend()
    ax.grid(which="major", linestyle=":", alpha=0.6)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(args.output, dpi=150)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
