import time
import ccxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pair = 'BTC/USDT'
binance = ccxt.binance()

def get_ob(pair=pair, lines:int=15):
    ob = binance.fetch_order_book(symbol=pair)
    def fill_df(ob:dict, askbid:str = 'bids', lines=lines):
        df = pd.DataFrame(ob[askbid], columns=['price', 'size'])
        df['type'] = pd.Series( [askbid for v in range(len(df.index))])
        df['category'] = pd.qcut(df['price'],lines).values
        df = df.groupby('category').agg({ 'price':'first', 'size':'sum', 'type':'first' }).set_index('price')
        return df    
    df = pd.concat([fill_df(ob,'bids'),fill_df(ob,'asks')])  
    return df

fig, ax = plt.subplots()

while True:
    df = get_ob(lines=12)
    colors = list(np.where(df['type']=='bids', 'red','blue'))
    ax = plt.barh(y=df.index, width=df['size'], color=colors,tick_label=df.index)  
    plt.show()
    time.sleep(1)


