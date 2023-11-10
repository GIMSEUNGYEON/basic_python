#가위바위보 만들깅
from random import random

while(True) :
    me = input("가위 바위 보 입력 : ")

    print('나 : ' + me) 
    
    mynum = 0;
    if me == '가위' : 
        mynum = 1
        break
    elif me == '바위' :
        mynum = 2
        break
    elif me == '보' :
        mynum = 3
        break
    else : 
        print('잘못된 입력!')
    
    
# print(mynum)

comnum = int(random()*3+1)
# print(comnum)

com = ''
if comnum == 1 :
    com = '가위'
elif comnum == 2 :
    com = '바위'
else :
    com = '보'
print('컴 : ' + com)

if (mynum - comnum) == -2 or  (mynum - comnum) == 1 :
    print('win!')
elif(mynum - comnum) == 0 : 
    print('무승부!')
    print('무승부!')
else :
    print('lose!')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    