# animal을 호출하는 human클래스
from day03.ooptest01 import Animal
# import하면 부모클래스의 print등이 자동으로 호출됨
# 부모 클래스에서 main을 사용하면 자식 클래스에서 호출되어도 
# 부모의 print가 다 출력되지는 않음
class Human(Animal):
    def __init__(self):
        self.asset = 0
        
    def gold(self, asset):
        self.asset = 10000000000
hum1 = Human()

hum1.named('사람')

print('사람이름 : ', hum1.name)

# hum1.gold(asset)

