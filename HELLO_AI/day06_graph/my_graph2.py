import matplotlib.pyplot as plt
import numpy as np

x = np.ones(4)
fig = plt.figure()

ax = fig.add_subplot(1,1,1, projection="3d")

ax.plot(x*0, [0,1,2,3], [0,5,0,5], 'r')

ax.plot(x, [0,1,2,3], [5,0,5,0], 'g')

ax.plot(x*2, [0,1,2,3], [2.5,2.5,2.5,2.5], 'b')

plt.show()
