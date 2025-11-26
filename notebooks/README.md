## Notebooks Overview

This folder contains the main analysis notebooks for the project **Predicting Price Moves with News Sentiment**. Each notebook corresponds to one task in the pipeline and builds on the previous work.

### `task_1_analysis.ipynb` – Exploratory News & Publisher Analysis

- **Goal**: Understand the structure, volume, and sources of the raw Benzinga analyst ratings dataset.
- **Key steps**:
  - Load `data/raw_analyst_ratings.csv` using the shared `scripts/data_loader.py`.
  - Basic cleaning and inspection (headline lengths, date parsing, publisher distribution).
  - Publisher and domain analysis to see which authors/outlets dominate the feed.
  - Time-series plots of article volume over time to highlight changes in coverage.
- **Takeaways**:
  - Confirms this is a Benzinga-centric feed (heavy concentration in a few authors).
  - Reveals a large spike in article volume around 2019–2020, which is important when training models later.

### `task_2_quantitative.ipynb` – Technical & Return-Based Stock Analysis

- **Goal**: Build a reusable quantitative pipeline for a single stock (AAPL) and compute core technical indicators and returns.
- **Key steps**:
  - Use `scripts/financial_analysis.FinancialAnalyzer` to pull daily AAPL price history via `yfinance`.
  - Add technical indicators (SMA, RSI, MACD) using TA‑Lib.
  - Compute **daily** and **cumulative** returns.
  - Visualise indicator correlations (heatmaps) and cumulative performance over time.
- **Takeaways**:
  - Provides a clean, well-tested structure for price data that Task 3 reuses for correlation work.

### `task_3_correlation.ipynb` – News Sentiment vs. AAPL Price Movements

- **Goal**: Quantify the linear relationship between **daily financial news sentiment** and **AAPL daily returns**.
- **Key steps**:
  - Load `raw_analyst_ratings.csv`, normalise timestamps, and extract a **calendar date** for each headline.
  - Apply VADER sentiment analysis (`vaderSentiment`) to get a **compound score per headline**.
  - Aggregate to **average daily sentiment** across all headlines.
  - Pull AAPL OHLCV data with `FinancialAnalyzer` and compute **daily percentage returns**.
  - Merge sentiment and returns on trading date, then compute **Pearson correlation** and plot a scatter of sentiment vs. returns.
- **Result**:
  - Pearson correlation between average daily sentiment and AAPL daily returns is approximately **0.04**, indicating a **very weak positive relationship**.

### How to Run the Notebooks

1. **Activate the project virtual environment** (from the repo root):
   - Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
   - macOS/Linux: `source venv/bin/activate`
2. Install dependencies if needed:
   - `pip install -r requirements.txt`
3. Launch Jupyter:
   - `jupyter notebook` or `jupyter lab`
4. Open the desired notebook in the `notebooks/` folder and run it top‑to‑bottom.


