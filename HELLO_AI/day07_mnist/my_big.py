import numpy as np
arr = [1,0,0,0,0,  2,0,0,3,0]
arr_np = np.array(arr)

print(arr_np)
arr_max = 0

for idx, i in enumerate(arr_np) :
    for j in arr_np :
        if i < j :
            arr_max = j
            
    if i == arr_max :
        print(idx)    
    
print("===========================")

temp = -1  
max_idx = 0
for idx, i in enumerate(arr_np) :
    if temp < i :
        temp = i
        max_idx = idx
    
print(temp)
print(max_idx)


print("===========================")

mymax = -1
for i in arr_np :
    if mymax < i :
        mymax = i
        
print(mymax)

for idx, i in enumerate(arr_np) :
    if i == mymax :
        print(idx)