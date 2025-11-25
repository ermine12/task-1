import pandas as pd
import yfinance as yf
import talib
import matplotlib.pyplot as plt

class FinancialAnalyzer:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def retrieve_data(self):
        """
        Fetches historical stock data using yfinance.
        """
        print(f"Fetching data for {self.ticker}...")
        self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date, auto_adjust=True)
        
        if isinstance(self.data.columns, pd.MultiIndex):
            self.data.columns = self.data.columns.get_level_values(0)
            
        print(f"Data loaded: {self.data.shape[0]} rows.")
        return self.data

    def add_indicators(self):
        """
        Calculates SMA, RSI, and MACD using TA-Lib.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call retrieve_data() first.")

        # Simple Moving Averages
        self.data['SMA_20'] = talib.SMA(self.data['Close'], timeperiod=20)
        self.data['SMA_50'] = talib.SMA(self.data['Close'], timeperiod=50)

        # RSI
        self.data['RSI'] = talib.RSI(self.data['Close'], timeperiod=14)

        # MACD
        macd, macd_signal, macd_hist = talib.MACD(
            self.data['Close'],
            fastperiod=12,
            slowperiod=26,
            signalperiod=9
        )
        self.data['MACD'] = macd
        self.data['MACD_Signal'] = macd_signal

        return self.data

    def calculate_metrics(self):
        """
        Calculates basic financial metrics.
        """
        self.data['Daily_Return'] = self.data['Close'].pct_change()
        self.data['Cumulative_Return'] = (1 + self.data['Daily_Return']).cumprod()
        return self.data

    def plot_analysis(self):
        """
        Visualizes the stock price and indicators.
        """
        plt.figure(figsize=(14, 10))
        
        # Price + SMA
        plt.subplot(2, 1, 1)
        plt.plot(self.data.index, self.data['Close'], label='Close')
        plt.plot(self.data.index, self.data['SMA_20'], label='SMA 20')
        plt.plot(self.data.index, self.data['SMA_50'], label='SMA 50')
        plt.title(f"{self.ticker} Price with Moving Averages")
        plt.legend()
        plt.grid()

        # RSI
        plt.subplot(2, 1, 2)
        plt.plot(self.data.index, self.data['RSI'], label='RSI', color='purple')
        plt.axhline(70, color='red', linestyle='--')
        plt.axhline(30, color='green', linestyle='--')
        plt.title("Relative Strength Index (RSI)")
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()
