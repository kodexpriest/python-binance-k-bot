import ccxt
import yfinance as yf
import pandas as pd
import pandas_ta as ta

exchange = ccxt.binance()

bars = exchange.fetch_ohlcv('BNBUSDT', timeframe='5m', limit=500)

df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

print(df)