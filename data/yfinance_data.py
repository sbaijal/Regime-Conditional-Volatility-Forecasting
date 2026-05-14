import yfinance as yfin
from config import ticker, OBSERVATION_START_DATE, OBSERVATION_END_DATE
def fetch_data():
    data = yfin.download(ticker, start=OBSERVATION_START_DATE, end=OBSERVATION_END_DATE, auto_adjust=False)[['Adj Close']]
    data = data.dropna()
    return data