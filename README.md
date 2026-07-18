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

Open notebooks under `notebooks/` with Jupyter or VS Code / Cursor (select the `.venv` interpreter).

## Project Structure

```
NamUs_Missing/
├── .venv/                 # Python virtual environment (not committed)
├── data/
│   ├── raw/               # Original downloads (gitignored)
│   └── processed/         # Cleaned tables (gitignored)
├── notebooks/
│   ├── 01_data_collection.ipynb   # Load raw CSV, clean, export processed
│   ├── 02_eda.ipynb               # Juvenile vs adult exploratory analysis
│   └── 03_modeling.ipynb          # Logistic regression + decision tree
├── models/                # Saved .joblib pipelines (gitignored)
├── reports/figures/       # Exported plots (gitignored)
├── scripts/               # Optional helper scripts
├── requirements.txt
├── .gitignore
├── DATA_DICTIONARY.md
├── ETHICS.md
└── README.md
```

## Analysis Pipeline

Run notebooks in order:

1. **`01_data_collection.ipynb`** — Read `data/raw/missing_persons.csv`, clean types/fields, write `data/processed/missing_persons_cleaned.csv`.
2. **`02_eda.ipynb`** — Build `age_group` (juvenile if `missing_age` is under 18, else adult); explore age, sex, race/ethnicity, city, and year patterns.
3. **`03_modeling.ipynb`** — Predict `age_group` from `biological_sex`, `state`, and `race_ethnicity` (not `missing_age`—that would leak the label). Compare logistic regression and a decision tree on a shared stratified train/test split; export figures and save models with `joblib`.

### Modeling outputs (local only)

| Path | Contents |
|------|----------|
| `models/logreg_age_group.joblib` | Best logistic regression pipeline |
| `models/tree_age_group.joblib` | Best decision tree pipeline |
| `reports/figures/*.png` | Coefficient/importance plots, confusion matrices, tree plot, model comparison |

Data, fitted models, and figures are listed in `.gitignore` so large or sensitive artifacts stay local. Re-run the notebooks to regenerate them.

## How to Work

1. Put the raw NamUs extract in `data/raw/missing_persons.csv`
2. Run `01` → `02` → `03` in `notebooks/`
3. Inspect plots in the notebooks or under `reports/figures/`
4. Load saved models from `models/` if needed outside the notebook

## Conventions

- Keep `data/raw/` as the immutable source of truth — never edit files in place.
- Write cleaned output only to `data/processed/`.
- Name notebooks in order (`01_…`, `02_…`, `03_…`).
- Large data files, models, and report figures stay local; only `.gitkeep` placeholders are tracked for those folders.

## Data Source

NamUs public database: https://namus.nij.ojp.gov/

This project works from a CSV extract placed in `data/raw/`. Collection/cleaning steps live in `notebooks/01_data_collection.ipynb`.

## AI Assistance

This project used Grok 4.5 as a lightweight assistant for setup and support—not as the author of the analysis. Help covered the base file structure, library recommendations, and other simple project tasks. All analysis and modeling code was written by me; Grok was used to error-check and troubleshoot when needed.
