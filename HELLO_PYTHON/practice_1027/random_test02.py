from random import random

odd = 0
even = 0

for i in range(10000000) : 
    rnd1 = random()
    if(rnd1 > 0.5) : 
        odd+=1
    else : 
        even+=1

print(odd)

print(even)

'''
주석
'''




