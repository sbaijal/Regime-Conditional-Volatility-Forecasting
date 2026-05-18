import yfinance as yfin
import numpy as np
from config import ticker, OBSERVATION_START_DATE, OBSERVATION_END_DATE
def fetch_data():
    data = yfin.download(ticker, start=OBSERVATION_START_DATE, end=OBSERVATION_END_DATE, auto_adjust=False)
    data = data.dropna()
    return data

def log_return_data():
    data = fetch_data()
    prices = data['Adj Close']
    returns = np.log(prices/prices.shift(1)).dropna()
    log_returns = returns * 100
    log_returns.columns = ['Log Percentage Returns']
    return prices, returns, log_returns