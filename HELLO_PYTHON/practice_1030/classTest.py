# 클래스를 이용해 계산기 만들기
class calculate:

    def __init__(self):
        self.result = 0

    def plus(self, a, b):
        self.result = a + b
        return self.result

    def minus(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = a / b
        return self.result

        
cal = calculate()

print(cal.plus(2, 3))
print(cal.minus(7, 5))
print(cal.multiply(8, 2))
print(cal.divide(9, 3))

