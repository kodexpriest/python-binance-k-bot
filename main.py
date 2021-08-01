#imports
import datetime, time, pprint
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

import mplfinance as mpf


#this project
import config

#pyton-binance
from binance.client import Client
from binance.enums import *

#const
SYMBOL = 'BTCUSDT'
client = Client( config.API_KEY, config.API_SECRET )

def get_candles(symbol:str = SYMBOL):
    full_candles = DataFrame(data=client.get_historical_klines(symbol=SYMBOL, interval=KLINE_INTERVAL_3MINUTE, start_str='3m', limit=20),
                             columns= ['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Quote', 'Trades', 'TBBAV', 'TBQAV', 'Ignore'])
    candles = full_candles.loc[:,['Open_time', 'Open', 'High', 'Low', 'Close']]             # menos columnas
    candles = candles.astype({'Open': float, 'High': float, 'Low': float, 'Close': float})  # de object a float64
    candles['Open_time'] = pd.to_datetime(candles['Open_time'])                             # de int a datetime
    candles.set_index(pd.DatetimeIndex(candles['Open_time']))                               # DateTimeINDEX (ty google)
    return candles

candles = get_candles()

mpf.plot(candles,type='candle')
mpf.show()