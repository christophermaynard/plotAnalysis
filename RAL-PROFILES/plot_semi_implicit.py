#!/usr/bin/env python3
"""Bar chart of semi_implicit_timestep max time against MPI rank count."""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FixedLocator, FuncFormatter

ROUTINE = "semi_implicit_timestep"
METRIC = "Total Max(s)"

# Fraction of the gap between adjacent rank counts that a thread group may fill.
GROUP_FILL = 0.8


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="Path to vernier_long.csv")
    parser.add_argument("-o", "--output", type=Path,
                        default=Path("semi_implicit_vs_ranks.png"))
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    sit = df[df["routine"] == ROUTINE].sort_values("mpi_ranks")

    threads = sorted(sit["threads"].unique())
    ticks = sorted(sit["mpi_ranks"].unique())

    # 392/441 and 784/882 sit only 0.05 decades apart, so groups are sized from
    # the tightest pair rather than a fixed width.
    gaps = np.diff(np.log10(ticks))
    group_dex = GROUP_FILL * gaps.min()
    bar_dex = group_dex / len(threads)
    colours = plt.get_cmap("viridis")(np.linspace(0.15, 0.8, len(threads)))

    fig, ax = plt.subplots(figsize=(11, 6))

    for i, nthreads in enumerate(threads):
        sub = sit[sit["threads"] == nthreads]
        ranks = sub["mpi_ranks"].to_numpy(dtype=float)
        times = sub[METRIC].to_numpy(dtype=float)

        # Offset and size the bars multiplicatively so they stay even in log x.
        centre = (i - (len(threads) - 1) / 2) * bar_dex
        left = ranks * 10 ** (centre - bar_dex / 2)
        right = ranks * 10 ** (centre + bar_dex / 2)

        ax.bar(left, times, width=right - left, align="edge",
               color=colours[i], edgecolor="black", linewidth=0.5,
               label=f"{nthreads} thread{'s' if nthreads > 1 else ''}")

        for x, y in zip((left + right) / 2, times):
            ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points",
                        xytext=(0, 4), ha="center", va="bottom",
                        rotation=90, fontsize=7)

    ax.set_xscale("log")
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_minor_locator(FixedLocator([]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    ax.set_xlabel("MPI ranks")
    ax.set_ylabel(f"{ROUTINE} {METRIC}")
    ax.set_title("RAL3 672x672 UK: semi-implicit timestep cost on EX1A")
    ax.legend(title="OpenMP threads")
    ax.margins(y=0.12)
    ax.grid(axis="y", linestyle=":", alpha=0.6)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(args.output, dpi=150)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
