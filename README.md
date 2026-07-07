# NamUs Data Science Project

Data science / machine learning / analysis project for the National Missing and Unidentified Persons System (NamUs).

NamUs is the U.S. national centralized repository for missing, unidentified, and unclaimed person cases. The public database contains rich structured and unstructured data (demographics, circumstances, physical descriptions, images, etc.) that can be used for statistical analysis, trend detection, geospatial work, and ML-assisted matching or prioritization.

## Data Sources

### Primary: NamUs Public Database
- **Site**: https://namus.nij.ojp.gov/ (or namus.gov)
- **Access**: Public search + there are community scrapers that use the underlying API/endpoints.
- Existing open source scrapers:
  - [Prepager/namus-scraper](https://github.com/Prepager/namus-scraper)
  - Projects like Marius-Knipp/NamUs-Matching have demonstrated full data pulls into JSON/structured form.

**Recommended approach for this project**:
- Start by exploring the public web interface.
- Build or adapt a scraper to pull Missing Persons, Unidentified Persons, and Unclaimed Persons records (respect robots / rate limits / terms).
- Store raw responses immutably (JSON or parquet).

### Complementary Public Data
- FBI Uniform Crime Reports (UCR) / NIBRS
- Census Bureau data (population, demographics by geography)
- CDC / vital statistics
- Weather / geography datasets for context
- Kaggle or FOIA releases if available

## Project Goals (Examples — define your own)

- Exploratory data analysis: geographic distribution, time trends, demographics of cases.
- Feature engineering and risk / solvability modeling.
- Geospatial analysis and hot-spot detection.
- Text/NLP on case narratives or descriptions.
- Image analysis (with care around sensitive content).
- Attempting to surface patterns that could help investigators (always secondary to official work).

**Important**: This is for research / public-interest data analysis. Respect all data use policies, privacy, and ethical considerations. Do not attempt to re-identify or contact individuals.

## Project Structure

This follows the same practical data-science layout used in sibling projects (src layout + notebooks for exploration):

```
NamUs/
├── README.md
├── .gitignore
├── requirements.txt
├── .env.example
├── pyproject.toml
│
├── data/
│   ├── raw/                 # Immutable scraped / downloaded data
│   ├── processed/           # Cleaned, joined, feature-ready tables
│   └── external/            # Third-party reference datasets
│
├── notebooks/
│   ├── 00_data_acquisition.ipynb
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_analysis.ipynb
│
├── src/
│   └── namus/               # Reusable Python package
│       ├── __init__.py
│       ├── config.py
│       ├── data/
│       ├── features/
│       ├── models/
│       └── utils/
│
├── scripts/                 # Standalone scripts (e.g. full scrape runner)
├── config/                  # Config files, case lists, parameters
├── models/                  # Saved models / artifacts
├── reports/
│   └── figures/
│
└── tests/
```

## Quick Start (PowerShell on Windows)

```powershell
# 1. Create and activate environment (already done during initial setup)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# Optional: install the local package in editable mode
pip install -e .

# 3. Set up local secrets
copy .env.example .env
# edit .env as needed
```

## Using the Package

```python
from namus.config import PROJECT_ROOT, DATA_RAW
import pandas as pd

print(PROJECT_ROOT)
# df = pd.read_parquet(DATA_RAW / "missing_persons.parquet")
```

## Recommended Workflow

1. **Acquisition** in `notebooks/00_data_acquisition.ipynb` (or a `scripts/scrape_namus.py`)
2. **EDA** in `01_eda.ipynb`
3. Keep raw data sacred in `data/raw/`
4. Move reusable code into `src/namus/`
5. Use parquet for large tabular data.

## Notes on Scraping NamUs

Community scrapers exist. Before writing your own:
- Review https://github.com/Prepager/namus-scraper
- Be polite (rate limiting, caching responses)
- Store full raw responses so you can re-process without re-hitting the site
- Handle updates / deltas carefully (cases get updated)

## License

MIT (or your choice — update as project evolves).

Contributions and ideas welcome for public-interest analysis of this important dataset.
