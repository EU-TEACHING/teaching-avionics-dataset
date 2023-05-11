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

ANOMALY_DIRS = ["LFBT_LFBL", "cputheft", "bpred"]  # , "speculate"]
ANOMALY_CLASSES = {"NOSTRESS": 0, "STSB": 1, "CPUTHEFT": 2, "BPRED": 3, "SPECTRE": 4}


def load_trace(
    anomaly: str,
    deployment: str,
    metrics_config_index: int,
    to_numpy: bool = False,
) -> Tuple[pd.DataFrame, bool]:
    metrics_config = METRICS_CONFIGS[metrics_config_index]
    measure_columns = [f"PMC{i}" for i in range(len(metrics_config))]
    measure_columns = ["DURATION"] + measure_columns

    dfs, core = [], None
    for num in range(metrics_config_index * 10, metrics_config_index * 10 + 10):
        df = pd.read_csv(f"../{anomaly}/{deployment}/raw_{num}.csv", sep=";")
        core = df["CORE"].unique()[0]
        df = df[df["PROBE"] != "MAF"]
        df[measure_columns] = df.groupby("MAF_COUNT")[measure_columns].transform("mean")
        df = df.groupby("MAF_COUNT").first()
        dfs.append(df)
    df = pd.concat(dfs).reset_index(drop=True)
    dependable = core < 4

    df = df.rename(
        {f"PMC{i}": c for i, c in enumerate(metrics_config)},
        axis=1,
    )
    if to_numpy:
        to_return = {"X": df[metrics_config].to_numpy(), "Y": df["CONTEXT"]}
    else:
        to_return = df

    return to_return, dependable


def load_dataset(metrics_config_index: int, train: bool = True):
    if train:
        deployments = {
            "LFBT_LFBL": ("xFTx.xx", "SFTS.xx"),
            "cputheft": ("xFTx.xx", "xUTx.xx"),
            "bpred": ("xFTx.xx", "xDTx.xx"),
        }
    else:
        deployments = {
            "LFBT_LFBL": ("ZFTZ.ZZ",),
            "cputheft": ("xVTx.xx",),
            "bpred": ("xGTx.xx",),
        }

    dfs = []
    for anomaly in ANOMALY_DIRS:
        for deployment in deployments[anomaly]:
            dfs.append(load_trace(anomaly, deployment, metrics_config_index)[0])

    df = pd.concat(dfs).reset_index(drop=True)
    df["CLASS"] = df["CONTEXT"].map(ANOMALY_CLASSES)
    return df
