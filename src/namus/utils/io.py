"""Common I/O helpers (parquet, json, etc.)."""
from pathlib import Path
import pandas as pd
from ..config import PARQUET_COMPRESSION


def save_parquet(df: pd.DataFrame, path: Path) -> None:
    """Save dataframe efficiently."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, compression=PARQUET_COMPRESSION, index=False)


def load_parquet(path: Path) -> pd.DataFrame:
    return pd.read_parquet(path)
