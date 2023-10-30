from random import random

arr = list(range(1, 45+1))

for i in range(100) :
    rnd = int(random()*len(arr))
    a = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = a

for x in range(6) :
    print(arr[x])
