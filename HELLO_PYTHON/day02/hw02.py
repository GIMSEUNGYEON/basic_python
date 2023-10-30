#업앤다운 게임
from random import random

com = int(random()*99+1)
cnt = 0

while True :    
    me = int(input("숫자를 입력하세요... "))
    if(com == me) :
        print("정답입니다!")
        break
    elif(com > me) : 
        print("UP")
    elif(com < me) :
        print("DOWN")
    
    cnt+=1
    
    if(cnt == 10) :
        print('도전 실패!!')
        print('정답은 {}입니다'.format(com))
        break