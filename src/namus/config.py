"""Project configuration, paths, and settings."""
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# Project root (two levels up from src/namus/config.py)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_EXTERNAL = PROJECT_ROOT / "data" / "external"

# Model and report directories
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Ensure directories exist
for d in [DATA_RAW, DATA_PROCESSED, DATA_EXTERNAL, MODELS_DIR, FIGURES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# API / source keys (add as needed)
# NAMUS_API_KEY = os.getenv("NAMUS_API_KEY")
# CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

# Common categories (customize as your analysis evolves)
CASE_TYPES = ["missing", "unidentified", "unclaimed"]

# Default date range for analysis (adjust)
DEFAULT_START_DATE = "2000-01-01"
DEFAULT_END_DATE = None  # None = latest available

# Storage
PARQUET_COMPRESSION = "zstd"
