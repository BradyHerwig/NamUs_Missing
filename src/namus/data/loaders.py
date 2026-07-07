"""Data loaders / scrapers for NamUs and related sources.

Add functions here such as:
- fetch_missing_persons()
- fetch_unidentified()
- load_raw_parquet(case_type)
"""
from pathlib import Path
import pandas as pd
from ..config import DATA_RAW


def example_loader() -> pd.DataFrame:
    """Placeholder. Replace with real acquisition logic."""
    # Example: return pd.read_parquet(DATA_RAW / "something.parquet")
    return pd.DataFrame()
