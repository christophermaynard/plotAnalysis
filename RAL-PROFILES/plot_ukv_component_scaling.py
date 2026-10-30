#!/usr/bin/env python3
"""Strong scaling of the main lfric_atm components against node count.

One panel per component; grouped bars per node count, one bar per OpenMP
thread count. Each bar is labelled with the per-rank local volume
(local_nx x local_ny columns).
"""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CORES_PER_NODE = 192  # Genoa
COMPONENTS = [
    "__lfric_atm__",
    "__setup__",
    "semi_implicit_timestep",
    "solver.mixed_solver",
    "dynamics.transport",
    "fast_physics",
    "slow_physics",
    "lfric_xios.read_fldg",
]
THREAD_COLOUR = {1: "firebrick", 2: "darkorange", 4: "gold"}
BAR_WIDTH = 0.16
BAR_SPACING = BAR_WIDTH
IDEAL_FROM = {10: ("k", "--"), 20: ("k", ":")}
# Fixed-cost components, where an ideal strong-scaling line is not meaningful.
NO_IDEAL = {"__setup__", "lfric_xios.read_fldg"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, nargs="+",
                        help="vernier_long.csv file(s); the fastest repeat "
                             "of each decomposition is kept.")
    parser.add_argument("-o", "--output", type=Path,
                        default=Path("ukv_component_scaling.png"))
    parser.add_argument("--metric", default="Total Max(s)")
    parser.add_argument("--title", default="UKV (960x1024 L70) strong scaling")
    args = parser.parse_args()

    df = pd.concat([pd.read_csv(p) for p in args.csv], ignore_index=True)
    df = df[df["routine"].isin(COMPONENTS)]
    df = df.loc[df.groupby(["decomposition", "routine"])[args.metric].idxmin()]
    df["nodes"] = (df["cores"] / CORES_PER_NODE).round().astype(int)
    nodes = sorted(df["nodes"].unique())
    xpos = {n: i for i, n in enumerate(nodes)}
    threads = sorted(df["threads"].unique())
    offset = {t: (i - (len(threads) - 1) / 2) * BAR_SPACING
              for i, t in enumerate(threads)}

    fig, axes = plt.subplots(2, 4, figsize=(20, 9.5), sharex=True)
    for ax, comp in zip(axes.flat, COMPONENTS):
        c = df[df["routine"] == comp]
        if c.empty:
            ax.set_visible(False)
            continue
        for t, g in c.groupby("threads"):
            x = [xpos[n] + offset[t] for n in g["nodes"]]
            bars = ax.bar(x, g[args.metric], width=BAR_WIDTH,
                          color=THREAD_COLOUR.get(t, "grey"),
                          edgecolor="black", linewidth=0.4, label=f"{t}T")
            for b, (_, r) in zip(bars, g.iterrows()):
                ax.text(b.get_x() + b.get_width() / 2, b.get_height() * 1.04,
                        f"{r.local_nx}x{r.local_ny}", rotation=90,
                        ha="center", va="bottom", fontsize=6)

        # Ideal scaling through the best time at each reference node count.
        for n_ref, (colour, style) in IDEAL_FROM.items():
            if n_ref not in xpos or comp in NO_IDEAL:
                continue
            t_ref = c.loc[c["nodes"] == n_ref, args.metric].min()
            ax.plot(range(len(nodes)), [t_ref * n_ref / n for n in nodes],
                    color=colour, ls=style, marker=".", lw=1,
                    label=f"ideal from {n_ref}n")

        n0, n1 = 10, nodes[-1]
        t0 = c.loc[c["nodes"] == n0, args.metric].min()
        best_hi = c.loc[c["nodes"] == n1, args.metric].min()
        ax.set_title(f"{comp}\n{t0:.1f} -> {best_hi:.1f} s "
                     f"({t0 / best_hi:.1f}x of {n1 / n0:.0f}x)",
                     fontsize=10)

        ax.set_yscale("log")
        ax.set_xticks(range(len(nodes)))
        ax.set_xticklabels([str(n) for n in nodes])
        ax.grid(True, axis="y", which="both", alpha=0.3)
        ax.set_ylim(top=ax.get_ylim()[1] * 1.8)
        if comp in NO_IDEAL:
            # Zoom the log axis so bar tops span ~0.3-0.7 of the panel height.
            lo, hi = np.log10(c[args.metric].min()), np.log10(c[args.metric].max())
            span = max((hi - lo) / 0.4, 0.3)
            mid = (lo + hi) / 2
            ax.set_ylim(10 ** (mid - span / 2), 10 ** (mid + span / 2))

    for ax in axes[1]:
        ax.set_xlabel("Nodes (192 cores each)")
    for ax in axes[:, 0]:
        ax.set_ylabel(f"{args.metric}")
    axes.flat[0].legend(fontsize=8)
    fig.suptitle(f"{args.title} - labels are local volume per MPI rank "
                 "(columns)", fontsize=12)
    fig.tight_layout()
    fig.savefig(args.output, dpi=150)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
