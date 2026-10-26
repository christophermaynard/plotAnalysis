#!/usr/bin/env python3
"""Bar charts of C896 component shares of the timestep and of the whole run."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TAGS = {"32x32_2T": 49, "32x16_2T": 98, "16x16_2T": 196}

TIMESTEP_PARTS = {
    "solver.mixed_solver": "Mixed solver",
    "dynamics.transport": "Transport",
    "slow_physics": "Slow physics",
    "fast_physics": "Fast physics",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="vernier_long.csv")
    parser.add_argument("-o", "--outdir", type=Path,
                        help="Output directory (default: beside the csv).")
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    t = df.pivot(index="routine", columns="decomposition",
                 values="Total Max(s)")[list(TAGS)]
    nodes = [str(n) for n in TAGS.values()]
    x = np.arange(len(nodes))

    fig1, ax1 = plt.subplots(figsize=(6, 5))
    fig2, ax2 = plt.subplots(figsize=(6, 5))

    width = 0.8 / len(TIMESTEP_PARTS)
    for i, (routine, label) in enumerate(TIMESTEP_PARTS.items()):
        pct = 100 * t.loc[routine] / t.loc["semi_implicit_timestep"]
        bars = ax1.bar(x + (i - (len(TIMESTEP_PARTS) - 1) / 2) * width,
                       pct, width, label=label)
        ax1.bar_label(bars, fmt="%.1f", fontsize=7)
    ax1.set_title("% of semi_implicit_timestep")
    ax1.set_ylabel("% of Total Max(s)")

    width = 0.35
    setup = 100 * t.loc["__setup__"] / t.loc["__lfric_atm__"]
    first = 100 * t.loc["gungho_driver.first_timestep"] / t.loc["__lfric_atm__"]
    b1 = ax2.bar(x - width / 2, setup, width, label="Setup")
    b2 = ax2.bar(x + width / 2, first, width, label="First timestep")
    b3 = ax2.bar(x, setup + first, 2 * width, fill=False, edgecolor="k",
                 linestyle="--", label="Setup + first timestep")
    for b in (b1, b2, b3):
        ax2.bar_label(b, fmt="%.1f", fontsize=7)
    ax2.set_title("% of __lfric_atm__")

    for ax in (ax1, ax2):
        ax.set_xticks(x, nodes)
        ax.set_xlabel("Nodes")
        ax.set_ylim(top=ax.get_ylim()[1] * 1.15)
        ax.legend(loc="upper left", ncol=2, fontsize=8)
        ax.grid(axis="y", alpha=0.3)

    outdir = args.outdir or args.csv.parent
    for fig, name in ((fig1, "c896_breakdown_timestep.png"),
                      (fig2, "c896_breakdown_setup.png")):
        fig.suptitle("C896 nwp_gal10 no_diags, 2 OpenMP threads, "
                     "720 timesteps")
        fig.tight_layout()
        fig.savefig(outdir / name, dpi=150)
        print(f"wrote {outdir / name}")


if __name__ == "__main__":
    main()
