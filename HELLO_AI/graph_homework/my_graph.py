import matplotlib.pyplot as plt
from graph_homework.data_gen import Data_gen
import numpy as np

x = np.arange(1,11)
y = np.ones(10)

fig = plt.figure()

ax = fig.add_subplot(1,1,1, projection="3d")

dg = Data_gen()

samX = dg.samsung_data()
lgX = dg.lg_data()
skX = dg.sk_data()
hanX = dg.han_data()
poX = dg.po_data()

# ax.plot(x,samX,y,'')
# ax.plot(x,lgX,y*2,'')
# ax.plot(x,skX,y*3,'')
# ax.plot(x,hanX,y*4,'')
# ax.plot(x,poX,y*5,'')

ax.plot(x,y,samX,'')
ax.plot(x,y*2,lgX,'')
ax.plot(x,y*3,skX,'')
ax.plot(x,y*4,hanX,'')
ax.plot(x,y*5,poX,'')

plt.show()
    
    
    
    
    
    
    
    
