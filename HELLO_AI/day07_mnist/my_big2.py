import numpy as np

arr = [0,5,0,0,1,  2,0,0,3,0]
arr_np = np.array(arr)

mymax = np.max(arr_np)

print("mymax",mymax)

myidx = np.argmax(arr_np)

print("myidx",myidx)