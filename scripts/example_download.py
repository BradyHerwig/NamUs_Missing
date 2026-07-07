"""Example script skeleton for data acquisition.

Replace with real logic for scraping or downloading NamUs data.
Run from project root: python scripts/example_download.py
"""
from pathlib import Path
import sys

# Make src importable when running script directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from namus.config import DATA_RAW

print("Project data raw dir:", DATA_RAW)
print("Add your download / scrape logic here.")
# Example future:
# data = fetch_namus_data()
# data.to_parquet(DATA_RAW / "missing_persons_raw.parquet")
