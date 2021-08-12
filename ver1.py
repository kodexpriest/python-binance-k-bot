import ccxt
import pandas as pd


binance = ccxt.binance()


ob = binance.fetch_order_book(symbol='BTC/USDT')
askdf = pd.DataFrame(ob['asks'], columns=['price', 'size'])
askdf['type'] = pd.Series( ['ask' for v in range(len(askdf.index))] )
biddf = pd.DataFrame(ob['bids'], columns=['price', 'size'])
biddf['type'] = pd.Series( ['bid' for v in range(len(biddf.index))] )
obdf = pd.concat([biddf, askdf])




print(obdf)