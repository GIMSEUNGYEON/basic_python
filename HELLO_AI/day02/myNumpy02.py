import numpy as np
arr = list(range(8))
arr_np = np.array(arr)

print(arr_np)
print(arr_np.shape) # 길이에 해당하는 첫번째 튜플만 반환

arr_n2 = np.reshape(arr_np, (2,4))

print(arr_n2)

print(arr_n2.shape)

arr_n3 = np.float16(arr_n2)

print(arr_n3)