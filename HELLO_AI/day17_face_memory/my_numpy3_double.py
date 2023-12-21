import numpy as np

arr = [1,2,3]


arr_n1 = np.array(arr)
arr_n2 = np.array(arr)

print(arr_n1)

arr_d = np.concatenate([arr_n1, arr_n2],0)

arr[0] = 4

print(arr_d)