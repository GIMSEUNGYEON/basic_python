import random

rnd1= random.random()
print('rnd1 : ', rnd1)
#원래 쓰던 그냥 랜덤
rnd2 = random.uniform(1,5)
print('rnd2 : ', rnd2)
#지정한 두 수 사이의(이상이하관계) 실수

rnd3 = random.randint(1, 5)
print('rnd3 : ', rnd3)
#지정한 두 수 사이의(이상이하관계) 정수

rnd4 = random.randrange(1, 5+1)
print('rnd4 : ', rnd4)
#range가 들어가면 이상 미만! 파라미터를 하나로 쓰는 것으로 0에서 시작할 수도 있음

arr = [1,2,3,4,5]
rnd5 = random.choice(arr)
print('rnd5 : ', rnd5)
#배열에서 임의의 숫자 뽑기

rnd6 = random.sample(arr, 2)
print('rnd6 : ', rnd6)
#배열에서 임의의 숫자 여러개 뽑기
#배열이 담고있는 값(value)가 중요한 것이 아닌 인덱스를 중복되지 않게 뽑음!
#예를 들어 ['a','b','a']
#가 있다면 arr[0]을 두번 뽑진 않지만 arr[2]는 뽑을 수 있음

rnd7 = random.shuffle(arr)
print('rnd7 : ', arr)
#배열의 숫자를 무작위로 바꾸어주는 함수. range는 읽기 전용이므로 list로 캐스팅해주어야만 사용할 수 있음




