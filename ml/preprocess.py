import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker='AAPL', period='1y'):
    """
    Download historical daily stock data for the given ticker and period.
    Default is Apple stock for the last 1 year.
    Returns a Pandas DataFrame.
    """
    stock_data = yf.Ticker(ticker)
    hist = stock_data.history(period=period)
    return hist

def preprocess_data(df):
    """
    Preprocess the data for modeling:
    - Create target variable as next day's closing price (shifted Close)
    - Drop any rows with NaN values
    - Select features (Close price) and target (Target)
    """
    df['Target'] = df['Close'].shift(-1)  # Next day's price
    df = df.dropna()
    X = df[['Close']]
    y = df['Target']
    return X, y
