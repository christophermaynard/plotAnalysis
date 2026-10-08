#!/usr/bin/env python3
"""Collate per-decomposition summarise-vernier tables into CSV for plotting."""

import argparse
import csv
from pathlib import Path

MESH = 672

# MPI ranks per task, as defined in rose-stem ral3_scale_configs.
RANKS = {
    "48x48_1T": 196, "48x48_2T": 98, "48x48_4T": 49,
    "24x24_1T": 784, "24x24_2T": 392, "24x24_4T": 196,
    "16x16_1T": 1764, "16x16_2T": 882, "16x16_4T": 441,
    "12x12_1T": 3136, "12x12_2T": 1568, "12x12_4T": 784,
    "8x8_1T": 7056, "8x8_2T": 3528, "8x8_4T": 1764,
}

METRICS = [
    "Total Min(s)", "Total Mean(s)", "Total Max(s)",
    "Self Min(s)", "Self Mean(s)", "Self Max(s)",
    "Max no. calls", "% time", "Time per call(s)",
]


def panel_decomp(ranks):
    """Most-square factorisation that divides the mesh in both directions.

    Reconstructs what panel_decomposition='auto' does; a process grid extent
    that does not divide the mesh cannot be partitioned.
    """
    candidates = [
        (d, ranks // d)
        for d in range(1, int(ranks**0.5) + 1)
        if ranks % d == 0 and MESH % d == 0 and MESH % (ranks // d) == 0
    ]
    if not candidates:
        raise ValueError(f"No valid panel decomposition for {ranks} ranks")
    return max(candidates)


def read_table(path):
    """Parse a summarise-vernier table into {routine: {metric: value}}."""
    rows = []
    for line in path.read_text().splitlines():
        if not line.strip().startswith("|"):
            continue
        rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    header, *body = rows
    return {r[0]: dict(zip(header[1:], r[1:])) for r in body}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("summary_dir", type=Path,
                        help="Directory of <tag>.txt summarise-vernier tables.")
    parser.add_argument("--pivot-metric", default="Total Max(s)",
                        choices=METRICS,
                        help="Metric used for the wide routine x decomposition "
                             "table.")
    args = parser.parse_args()

    tables = {}
    for path in sorted(args.summary_dir.glob("*.txt")):
        tag = path.stem
        if tag not in RANKS:
            continue
        tables[tag] = read_table(path)

    if not tables:
        raise SystemExit(f"No recognised summary tables in {args.summary_dir}")

    # Order by cores then threads so subgroups stay together.
    def sort_key(tag):
        threads = int(tag.split("_")[1].rstrip("T"))
        return (RANKS[tag] * threads, threads)

    tags = sorted(tables, key=sort_key)

    long_path = args.summary_dir / "vernier_long.csv"
    with open(long_path, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow([
            "decomposition", "subgroup", "threads", "mpi_ranks", "cores",
            "nx", "ny", "local_nx", "local_ny", "columns_per_rank", "routine",
        ] + METRICS)
        for tag in tags:
            subgroup, thread_str = tag.split("_")
            threads = int(thread_str.rstrip("T"))
            ranks = RANKS[tag]
            nx, ny = panel_decomp(ranks)
            lx, ly = MESH // nx, MESH // ny
            for routine, metrics in tables[tag].items():
                writer.writerow([
                    tag, subgroup, threads, ranks, ranks * threads,
                    nx, ny, lx, ly, lx * ly, routine,
                ] + [metrics.get(m, "") for m in METRICS])

    # Wide table: every routine seen anywhere, blank where a tag lacks it.
    routines = sorted({r for t in tables.values() for r in t})
    wide_path = args.summary_dir / "vernier_wide.csv"
    with open(wide_path, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["routine"] + tags)
        for routine in routines:
            writer.writerow(
                [routine]
                + [tables[t].get(routine, {}).get(args.pivot_metric, "")
                   for t in tags]
            )

    print(f"{len(tags)} decompositions, {len(routines)} routines")
    print(f"wrote {long_path}")
    print(f"wrote {wide_path} ({args.pivot_metric})")


if __name__ == "__main__":
    main()
