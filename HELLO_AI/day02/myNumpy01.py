import numpy as np

arr = [1,2,3]

arr_np = np.array(arr)

arr3 = arr * 3

arr_np3 = arr_np * 3

print(arr)      # 1,2,3
print(arr_np)   # 1 2 3
print(arr3)     # 1,2,3,1,2,3,1,2,3
print(arr_np3)  # 3 6 9