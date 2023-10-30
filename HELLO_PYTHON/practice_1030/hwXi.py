class Xi :
    def __init__(self):
        self.money = 1000
    def spend(self, cost):
        self.money -= cost
        return self.money
    def __del__(self):
        print("소멸자 호출")
class Putin :
    def __init__(self):
        self.cnt_nuclear = 10000;
    def war(self):
        self.cnt_nuclear-=1
        return self.cnt_nuclear
    def __del__(self):
        print("소멸자 호출")
    
x = Xi()


print(x.spend(10))

p = Putin()

print(p.war())
print(p.war())
print(p.war())
print(p.war())
print(p.war())
print(p.war())