#imports
import datetime, time
from pprint import pprint as pp
import config #binance api key and secret
import pandas as pd
import pandas_ta as ta

from binance.client import Client
from binance.enums import KLINE_INTERVAL_1MINUTE

#const
SYMBOL = 'BTCUSDT'
client = Client(config.API_KEY, config.API_SECRET)


#functions
def get_candles(symbol:str = SYMBOL, limit:int = 500):
    full_candles = pd.DataFrame(data=client.get_klines(
        symbol=symbol,
        interval=KLINE_INTERVAL_1MINUTE,
        limit=limit),
        columns= ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Quote', 'Trades', 'TBBAV', 'TBQAV', 'Ignore'])
    candles = full_candles.loc[:limit,['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]                            # menos columnas
    candles = candles.astype({'Open': float, 'High': float, 'Low': float, 'Close': float, 'Volume': float})         # de object a float64
    candles['Date'] = pd.to_datetime(candles['Date'])                                                               # de int a datetime
    candles.set_index('Date', inplace=True)
    
    atr = candles.ta.atr(length=5)
    result = pd.concat([candles, atr], axis=1)
    return result

def candles(limit:int = 10):
    candles = get_candles(limit=limit)
    return candles.to_html()

def get_balance():
    balance = {}
    b = client.futures_account_balance()
    for k,v in enumerate(b):
        balance.update({k:{'asset':v['asset'],'balance':v['balance']}})
    return balance

def get_info():
    info = client.get_exchange_info()
    return info

def get_orders():
    orders = client.futures_get_open_orders()
    return orders

#app0
if __name__ == '__main__':
    print(get_candles(symbol='ETHUSDT',limit=1))
    print(get_balance())
