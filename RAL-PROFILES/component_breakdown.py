#!/usr/bin/env python3
"""Top-level component totals across decompositions.

Vernier callipers nest, so total times double-count. Comparing them is only
meaningful within one level of the tree; these are the phases of __lfric_atm__
and, inside the timestep, the children of semi_implicit_timestep.
"""

import argparse
from pathlib import Path

import pandas as pd

PARENT = "__lfric_atm__"
METRIC = "Total Max(s)"

# These three partition __lfric_atm__ exactly; initialise and mesh_init are
# inside __setup__, not beside it.
PHASES = [
    "gungho_driver.timestep",
    "__setup__",
    "gungho_driver.first_timestep",
]

# Science components one level below gungho_driver.timestep.
COMPONENTS = [
    "dynamics.transport",
    "slow_physics",
    "fast_physics",
    "dynamics.compute_si_operators",
    "dynamics.solver",
    "dynamics.rhs_alg",
    "gungho_diagnostics_driver",
    "mass_matrix_solver_alg",
    "dynamics.phys_predictors",
    "dynamics.transport_predictors",
    "update_lbcs",
    "dynamics.rhs_lbc",
]

# Cross-cutting leaves, called from inside the components rather than beside
# them, so they are reported separately and not summed with them.
MEMOS = ["field.halo_ex_1", "lfric_xios.read_fldg", "semi_implicit_timestep"]

ORDER = ["48x48_1T", "48x48_2T", "48x48_4T",
         "24x24_1T", "24x24_2T", "24x24_4T",
         "16x16_1T", "16x16_2T", "16x16_4T",
         "12x12_4T",
         "8x8_1T", "8x8_2T", "8x8_4T"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, nargs="+")
    parser.add_argument("--percent", action="store_true",
                        help="Express each component as a % of the parent.")
    parser.add_argument("--relative-to", default=PARENT,
                        help="Calliper the percentages are taken against.")
    args = parser.parse_args()

    df = pd.concat([pd.read_csv(p) for p in args.csv], ignore_index=True)
    df = df.loc[df.groupby(["decomposition", "routine"])[METRIC].idxmin()]

    wide = df.pivot(index="routine", columns="decomposition", values=METRIC)
    cols = [c for c in ORDER if c in wide.columns]
    wide = wide[cols]

    parent = wide.loc[args.relative_to]

    def block(names, label):
        rows = wide.loc[[n for n in names if n in wide.index]]
        return rows.loc[rows.mean(axis=1).sort_values(ascending=False).index]

    phases = block(PHASES, "phase")
    comps = block(COMPONENTS, "component")
    memos = wide.loc[[m for m in MEMOS if m in wide.index]]

    if args.percent:
        phases, comps, memos = (100 * t / parent for t in (phases, comps, memos))
        fmt = "{:6.1f}".format
    else:
        fmt = "{:7.1f}".format

    table = pd.concat([
        pd.DataFrame({c: [100.0 if args.percent else parent[c]]
                      for c in cols}, index=[f"{PARENT}  (whole run)"]),
        phases,
        pd.DataFrame({c: [float("nan")] for c in cols},
                     index=["-- inside gungho_driver.timestep --"]),
        comps,
        pd.DataFrame({c: [comps.sum()[c]] for c in cols},
                     index=["sum of components"]),
        pd.DataFrame({c: [float("nan")] for c in cols}, index=["-- memo --"]),
        memos,
    ])

    unit = f"% of {args.relative_to}" if args.percent else "seconds"
    print(f"{METRIC}, {unit}, best of {len(args.csv)} run(s)\n")
    print(table.to_string(float_format=fmt, na_rep=""))

    if args.percent:
        spread = pd.concat([phases, comps])
        print(f"\nconsistency across decompositions (% of {args.relative_to}):\n")
        summary = pd.DataFrame({
            "min": spread.min(axis=1),
            "max": spread.max(axis=1),
            "range": spread.max(axis=1) - spread.min(axis=1),
        })
        print(summary.to_string(float_format="{:6.1f}".format))


if __name__ == "__main__":
    main()
