import matplotlib.pyplot as plt
import numpy as np
from day06_graph.daostock import DaoStock


ds = DaoStock()

s_names  = ds.select_name()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

prices = []
for i in s_names:
    prices.append(ds.select(i))

x = np.ones(len(prices[0]), dtype=np.int8)
y = np.arange(0, len(prices[0]))

for idx, i in enumerate(prices):
    ax.plot(x*idx, y, i, '')

plt.show()
    
    
    
    
    
