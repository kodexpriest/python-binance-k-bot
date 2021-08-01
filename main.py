#imports
import datetime, time, pprint

from matplotlib.pyplot import tight_layout
import config #binance api key and secret
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from binance.client import Client
from binance.enums import KLINE_INTERVAL_1MINUTE

#const
SYMBOL = 'BNBUSDT'
client = Client(config.API_KEY, config.API_SECRET)

def get_candles(symbol:str = SYMBOL, limit:int = 500):
    full_candles = pd.DataFrame(data=client.get_klines(
        symbol=SYMBOL,
        interval=KLINE_INTERVAL_1MINUTE,
        limit=limit),
        columns= ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Quote', 'Trades', 'TBBAV', 'TBQAV', 'Ignore'])
    candles = full_candles.loc[:limit,['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]                            # menos columnas
    candles = candles.astype({'Open': float, 'High': float, 'Low': float, 'Close': float, 'Volume': float})     # de object a float64
    candles['Date'] = pd.to_datetime(candles['Date'])                                                           # de int a datetime
    candles.set_index('Date', inplace=True)
    return candles

candles = get_candles(limit=500)

print(candles)