import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as ani

from pprint import pprint as pp

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(1,1,1)
ax.set_title('BIDS')

x, y = [], []

def get_data():
    data = requests.get("https://api.pro.coinbase.com/products/BTC-USD/book?level=2").json()
    bids = pd.DataFrame(data['bids'], columns=['bid', 'bid size', 'q']).astype(float).iloc[:,:2]
    asks = pd.DataFrame(data['asks'], columns=['ask', 'ask size', 'q']).astype(float).iloc[:,:2]
    df = pd.concat([bids, asks])
    return df

def plot():
    df = get_data()
    y = df['bid']
    x = df['bid size']
    ax.barh(y, x)
    return ax

ani.FuncAnimation(fig, plot, interval=30)
plt.show()
    
    


ani.FuncAnimation()
    
