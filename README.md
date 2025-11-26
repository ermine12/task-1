## Predicting Price Moves with News Sentiment

This project explores how financial news sentiment relates to equity price movements, using a Benzinga analyst ratings dataset and daily stock price data.

### Project Structure

- **`data/`**
  - `raw_analyst_ratings.csv`: Raw Benzinga-style news headlines with timestamps, publisher, URL, and stock ticker.
  - `AAPL.csv`: Example price series (CSV) for Apple, used in early experiments.
- **`notebooks/`**
  - `task_1_analysis.ipynb`: Exploratory analysis of the news dataset (headline lengths, publishers, time-series volume).
  - `task_2_quantitative.ipynb`: Quantitative AAPL analysis (technical indicators, daily and cumulative returns).
  - `task_3_correlation.ipynb`: Correlation between daily news sentiment and AAPL daily returns.
  - `README.md`: High-level documentation for all notebooks.
- **`scripts/`**
  - `data_loader.py`: Shared CSV loader that normalises timestamps and checks required columns.
  - `descriptive.py`, `text_analysis.py`, `time_series.py`: Utilities for Task 1 descriptive and text analysis.
  - `financial_analysis.py`: `FinancialAnalyzer` class used in Tasks 2–3 to fetch price data and compute indicators/returns.
- **`tests/`**
  - `test_loader.py`: Basic tests for the data loader.

### Tasks Overview

- **Task 1 – News & Publisher Exploration**
  - Understand dataset size, headline structure, and publisher distribution.
  - Identify volume spikes and potential biases (e.g., Benzinga-specific editorial style).

- **Task 2 – Stock Price & Indicator Analysis**
  - Build a reproducible AAPL price pipeline with technical indicators (SMA, RSI, MACD).
  - Compute daily and cumulative returns; inspect indicator correlations and performance.

- **Task 3 – Correlation Between News and Stock Movement**
  - Apply VADER sentiment analysis to news headlines, aggregate to daily sentiment.
  - Align daily sentiment with AAPL daily returns and compute the Pearson correlation coefficient.
  - Result: correlation ≈ **0.04**, indicating a **very weak positive relationship** between market-wide news sentiment and one-day AAPL returns.

### Environment & Dependencies

- Python 3.10 (virtual environment under `venv/`).
- Key libraries (see `requirements.txt`):
  - `pandas`, `numpy`, `matplotlib`, `seaborn`
  - `yfinance`, `TA-Lib`
  - `textblob`, `vaderSentiment`, `scikit-learn`

To get started:

```bash
# from the project root
python -m venv venv
.\venv\Scripts\Activate.ps1  # on Windows PowerShell
pip install -r requirements.txt
```

Then open the notebooks under `notebooks/` and run each one top‑to‑bottom.


