#!/usr/bin/env python3
"""UKV XIOS read scaling against XIOS node count.

Panel 1: lfric_xios.read_fldg from Vernier (ukv_xios and ukv_xios8pn runs).
Panels 2-5: per-file read time from MPICH MPI-IO stats in job.err
(ukv_xios_io runs), taken as total bytes / net read bandwidth for every
collective open of the file. Bars are coloured by XIOS ranks per node.
"""

import argparse
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

PER_NODE_COLOUR = {8: "royalblue", 16: "teal"}
BAR_WIDTH = 0.35
FILES = {
    "GLOMAP aerosol": "glomap",
    "LBC": "lbc_",
    "Start dump": "checkpoint_um2lfric",
    "Ozone": "ozone",
}
TAG_RE = re.compile(r"_xios(\d+)r(\d+)n")


def parse_mpiio(job_err):
    """Return {file label: seconds} summed over every read of that file."""
    totals = {k: 0.0 for k in FILES}
    fname, nbytes = None, 0
    for line in job_err.read_text(errors="replace").splitlines():
        if "MPIIO read access patterns for" in line:
            fname = line.split(" for ", 1)[1].strip()
            nbytes = 0
        elif "total bytes for reads" in line:
            nbytes = int(line.split("=")[1].split()[0])
        elif "net read BW (MiB/s)" in line and fname:
            bw = float(line.split("=")[1])
            if bw > 0:
                for label, key in FILES.items():
                    if key in fname:
                        totals[label] += nbytes / (bw * 2**20)
            fname = None
    return totals


def bars(ax, data, ylabel):
    """data: DataFrame with xios_nodes, per_node, ranks, value."""
    nodes = sorted(data["xios_nodes"].unique())
    xpos = {n: i for i, n in enumerate(nodes)}
    per_nodes = sorted(data["per_node"].unique())
    offset = {p: (i - (len(per_nodes) - 1) / 2) * BAR_WIDTH
              for i, p in enumerate(per_nodes)}
    for p in per_nodes:
        g = data[data["per_node"] == p]
        b = ax.bar([xpos[n] + offset[p] for n in g["xios_nodes"]], g["value"],
                   width=BAR_WIDTH, color=PER_NODE_COLOUR[p],
                   edgecolor="black", linewidth=0.4,
                   label=f"{p} XIOS ranks/node")
        for rect, r in zip(b, g["ranks"]):
            ax.text(rect.get_x() + rect.get_width() / 2,
                    rect.get_height(), f"{r}r\n{rect.get_height():.1f}s",
                    ha="center", va="bottom", fontsize=7)
    ax.set_xticks(range(len(nodes)))
    ax.set_xticklabels([str(n) for n in nodes])
    ax.set_xlabel("XIOS nodes")
    ax.set_ylabel(ylabel)
    ax.set_ylim(top=data["value"].max() * 1.25)
    ax.grid(True, axis="y", alpha=0.3)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vernier", type=Path, nargs="+",
                        default=[Path("ukv_xios/summaries/vernier_long.csv"),
                                 Path("ukv_xios8pn/summaries/vernier_long.csv")])
    parser.add_argument("--mpiio-dir", type=Path, default=Path("ukv_xios_io"))
    parser.add_argument("--threads", type=int, default=1,
                        help="Thread count of the Vernier runs to plot.")
    parser.add_argument("--metric", default="Total Max(s)")
    parser.add_argument("-o", "--output", type=Path,
                        default=Path("ukv_xios_io/ukv_xios_read_scaling.png"))
    args = parser.parse_args()

    v = pd.concat([pd.read_csv(p) for p in args.vernier], ignore_index=True)
    v = v[(v["routine"] == "lfric_xios.read_fldg") & (v["threads"] == args.threads)]
    vern = pd.DataFrame({"xios_nodes": v["xios_nodes"],
                         "per_node": v["xios_per_node"],
                         "ranks": v["xios_ranks"],
                         "value": v[args.metric]})

    rows = []
    for job_err in sorted(args.mpiio_dir.glob("run_lfric_atm_*/*/job.err")):
        m = TAG_RE.search(job_err.parent.parent.name)
        ranks, nodes = int(m.group(1)), int(m.group(2))
        for label, secs in parse_mpiio(job_err).items():
            rows.append({"file": label, "xios_nodes": nodes,
                         "per_node": ranks // nodes, "ranks": ranks,
                         "value": secs})
    mpiio = pd.DataFrame(rows)

    fig, axes = plt.subplots(2, 3, figsize=(16, 9.5))
    axes = axes.flat
    bars(axes[0], vern, f"{args.metric}")
    axes[0].set_title(f"lfric_xios.read_fldg ({args.threads}T)\nVernier",
                      fontsize=10)
    axes[0].legend(fontsize=8, loc="upper right")
    for ax, label in zip(axes[1:], FILES):
        bars(ax, mpiio[mpiio["file"] == label], "Read time (s)")
        ax.set_title(f"{label}\nMPI-IO stats (bytes / net read BW)",
                     fontsize=10)
    for ax in axes[1 + len(FILES):]:
        ax.set_visible(False)
    fig.suptitle("UKV 16x16 (20 model nodes): read time vs XIOS nodes",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(args.output, dpi=150)
    print(f"Wrote {args.output}")
    print(mpiio.pivot_table(index="file", columns=["ranks", "xios_nodes"],
                            values="value").round(2))


if __name__ == "__main__":
    main()
