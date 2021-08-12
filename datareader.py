from datetime import datetime, timedelta
import pandas_ta as ta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ini_date = (datetime.now() - timedelta(7)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

df = web.DataReader('BTC-USD', data_source = 'yahoo', start=ini_date, end=end_date)

plt.plot(df['Adj Close'])
plt.show()