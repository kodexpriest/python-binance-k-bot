import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


r = requests.get("https://api.binance.com/api/v3/depth",
                 params=dict(symbol="BTCUSDT"))
results = r.json()

fram = 

frames = {side: pd.DataFrame(data=results[side], columns=["price", "quantity"],
                             dtype=float)
          for side in ["bids", "asks"]}


frames_list = [frames[side].assign(side=side) for side in frames]
data = pd.concat(frames_list, axis="index", 
                 ignore_index=True, sort=True)




fig, ax = plt.subplots()



sns.ecdfplot(x="price", weights="quantity", stat="count", complementary=True, data=frames["bids"], ax=ax)
sns.ecdfplot(x="price", weights="quantity", stat="count", data=frames["asks"], ax=ax)
sns.scatterplot(x="price", y="quantity", hue="side", data=data, ax=ax)

ax.set_xlabel("Price")
ax.set_ylabel("Quantity")

plt.show()