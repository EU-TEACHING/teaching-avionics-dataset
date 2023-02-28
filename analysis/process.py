from typing import Tuple
import pandas as pd


METRICS_CONFIGS = [
    [
        "L1D_CACHE",
        "L1D_CACHE_REFILL",
        "L1D_CACHE_WB",
        "L2D_CACHE",
        "L2D_CACHE_REFILL",
        "L2D_CACHE_WB",
    ],
    [
        "INST_RETIRED",
        "LD_RETIRED",
        "ST_RETIRED",
        "BR_PRED",
        "BR_MIS_PRED",
        "PREFETCH",
    ],  # speculate, 4th anomaly
    [
        "LD_SPEC",
        "ST_SPEC",
        "BR_PRED",
        "DP_SPEC",
        "VFP_SPEC",
        "L1I_CACHE_REFILL",
    ],  # speculate, 4th anomaly
    ["LD_SPEC", "ST_SPEC", "L1D_CACHE", "INST_SPEC", "L1I_CACHE", "L1I_CACHE_REFILL"],
    [
        "L1D_TLB_REFILL",
        "L1I_TLB_REFILL",
        "L1D_CACHE",
        "L1I_CACHE",
        "BUS_ACCESS",
        "MEM_ACCESS",
    ],
]


def load_trace(
    anomaly: str,
    deployment: str,
    metrics_config_index: int,
    to_numpy: bool = False,
) -> Tuple[pd.DataFrame, bool]:
    dfs = [
        pd.read_csv(f"../{anomaly}/{deployment}/raw_{num}.csv", sep=";")
        for num in range(metrics_config_index * 10, metrics_config_index * 10 + 10)
    ]
    df = pd.concat(dfs)
    df = df[df["PROBE"] != "MAF"]
    core = df["CORE"].unique()[0]

    dependable = core < 4
    metrics_config = METRICS_CONFIGS[metrics_config_index]
    df = df.rename({f"PMC{i}": c for i, c in enumerate(metrics_config)}, axis=1)
    df = df[["TIMESTAMP", "DURATION"] + metrics_config + ["CONTEXT"]]
    if to_numpy:
        to_return = {"X": df[metrics_config].to_numpy(), "Y": df["CONTEXT"]}
    else:
        to_return = df

    return to_return, dependable
