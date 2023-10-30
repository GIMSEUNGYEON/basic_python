from random import random

com = int(random()*99 + 1)

for i in range(10) :
    mine = input("숫자를 입력하세요")
    imine = int(mine)
    if com > imine :
        print(f"{mine} : up")
    elif com < imine :
        print(f"{mine} : down")
    else :
        print(f"{mine} : 정답입니다!")
        break
