# NamUs Data Science Project

Data science project for the National Missing and Unidentified Persons System (NamUs).

Through this project and modeling, the question I sought to answer was: **How do demographic and geographic characteristics of NamUs missing-person listings differ between juveniles and adults, and which factors best distinguish the two groups when modeled with logistic regression versus a decision tree?** I sought to answer this because national averages can hide different listing profiles by age group, and comparing an interpretable regression model to a tree shows whether simple additive effects are enough or whether interactions matter—while staying honest that this describes patterns in a public listing database, not the true risk of going missing.

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

## AI Assistance

This project used Grok 4.5 as a lightweight assistant for setup and support—not as the author of the analysis. Help covered the base file structure, library recommendations, and other simple project tasks. All analysis and modeling code was written by me; Grok was used to error-check and troubleshoot when needed.
