# NamUs Data Science Project

Data science project for the National Missing and Unidentified Persons System (NamUs).

## Quick Start (PowerShell)

```powershell
# First time only — create the virtual environment
python -m venv .venv

# Activate the environment (do this every new terminal session)
.\.venv\Scripts\Activate.ps1

# Install packages (only needed once, or after requirements change)
pip install -r requirements.txt
```

## Project Structure

```
NamUs_Missing/
├── .venv/                 # Python virtual environment (not committed)
├── data/
│   ├── raw/               # Original downloaded data (never edit)
│   └── processed/         # Cleaned / ready-to-use data
├── notebooks/             # EDA, analysis, and modeling
├── models/                # Saved models and predictions
├── reports/figures/       # Exported plots for write-ups
├── scripts/               # Standalone helper scripts
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Work

1. Put raw data downloads into `data/raw/`
2. Do data setup and EDA in `notebooks/`
3. Save cleaned data to `data/processed/`
4. Save trained models to `models/`

## Conventions

- Keep `data/raw/` as the immutable source of truth — never edit files in place.
- Name notebooks in order (e.g. `01_data_collection.ipynb`, `02_eda.ipynb`, `03_modeling.ipynb`).
- Large data files and models stay local; only `.gitkeep` placeholders are tracked in git.

## Data Source

NamUs public database: https://namus.nij.ojp.gov/

You can use existing community scrapers or build your own with `requests` and `beautifulsoup4`.

## Optional Extras

Add packages to `requirements.txt` only when a notebook needs them (e.g. `plotly`, `xgboost`, `statsmodels`).