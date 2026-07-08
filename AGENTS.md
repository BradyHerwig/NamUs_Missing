# Project conventions

## Layout

- **Notebooks** live in `notebooks/` — all analysis, EDA, and modeling work happens here.
- **Data** lives in `data/raw/` (original downloads) and `data/processed/` (cleaned tables).
- **Models** live in `models/` as saved files (`.joblib`, `.pkl`), not as notebooks.
- **Figures** for reports go in `reports/figures/`.

## Notebooks

- Use numbered notebooks: `01_data_collection.ipynb`, `02_eda.ipynb`, `03_modeling.ipynb`.
- Do not put notebooks inside `data/` or `models/`.
- The author writes all markdown explanations manually — do not add narrative markdown cells.
- Keep notebook changes to code and minimal section headers only.

## Data

- Treat `data/raw/` as immutable. Never edit files in place.
- Write cleaned output to `data/processed/`.
- Be careful with personally identifying fields and images.

## AI assistants

- Do not write analysis code unless explicitly asked.
- Do not fill in `DATA_DICTIONARY.md` or `ETHICS.md` — the author maintains those.