from random import random

def getHollJJak(num):
        if(num%2 == 0) :
            return "짝"
        else : 
            return "홀"
            

rnd = int(random()*99)+1
print(rnd)
com = getHollJJak(rnd)

print(com)

#//////////////////////////////////////////////////////////////

def getHollJJak2():
    com = ''
    rnd = random()
    if rnd > 0.5 : 
        return '홀'
    else :
        return '짝'
    
com = getHollJJak2()
print(com)