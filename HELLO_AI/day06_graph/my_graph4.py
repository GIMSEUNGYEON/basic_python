import matplotlib.pyplot as plt
import numpy as np
from day06_graph.daostock import DaoStock

ds = DaoStock()

s_names  = ds.select_name()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

prices = []
for i in s_names:
    prices.append(ds.selectArrN(i))
    
x = np.ones(len(prices[0]), dtype=np.int8)
y = np.arange(0, len(prices[0]))

for idx, i in enumerate(prices):
    tp = i/prices[idx][0]*100
    ax.plot(x*idx, y, tp, '')

ax.set_xlabel('Stock Index')
ax.set_ylabel('Time')
ax.set_zlabel('Price Percentage Change')

plt.show()



