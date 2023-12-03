import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(1,1,1, projection="3d")

ax.plot([0,0,0], [0,2,4], [0,5,0], 'r')

ax.plot([0,0,0], [0,2,4], [0,-5,0], 'g')

ax.plot([3,3,3], [0,2,4], [0,-5,0], color='orange')

ax.plot([3,3,3], [0,2,4], [0,0,0], color='orange')

ax.plot([0,2,0], [0,2,4], [0,0,0], '')

ax.plot([0,-2,0], [0,2,4], [0,0,0], '')

plt.show()
