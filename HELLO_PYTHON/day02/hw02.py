#업앤다운 게임
from random import random

com = int(random()*99+1)
cnt = 0

while True :    
    me = int(input("숫자를 입력하세요... "))
    cnt+=1
    print("시도횟수: ", cnt)
    if(com == me) :
        print("정답입니다!")
        break
    elif(com > me) : 
        print("UP")
    elif(com < me) :
        print("DOWN")
    
    
    if(cnt == 10) :
        print('도전 실패!!')
        # print('정답은 {}입니다'.format(com))
        print(f'정답은 {com}입니다')
        break