import numpy as np
from day10mnist_image.my_numpy import arr_n

arr = [[[1],[2],[3]], [[4],[5],[6]]]
arr_n = np.array(arr)

print(arr)
print(arr_n)

np.save("arr_n", arr_n)

