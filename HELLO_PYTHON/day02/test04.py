# 홀짝을 선택하시오
from random import random

# me = input("홀짝을 선택하시오")

# print('나 : ' + me)
rnd = random()

print(rnd)
com = ''
if rnd < 0.5 : 
    com = '홀'
else :
    com = '짝'

print('컴 : ' + com)

# if me == com : 
#     print("결과 : 승리")
# else : 
#     print("결과 : 패배")
#
