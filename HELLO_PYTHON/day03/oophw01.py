class Xi : 
    def __init__(self):
        self.money = 1000
    def spend(self, cost):
        self.money -= cost
        return self.money
    def __del__(self):
        print("소멸자")
        
class Putin : 
    def __init__(self):
        self.cnt_nuclear = 10000
    def war(self):
        self.cnt_nuclear -=1
        return self.cnt_nuclear
    def __del__(self):
        print("소멸자")

class Minkyu(Xi, Putin) : 
    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
        
if __name__ == "__main__" :
    desc = Minkyu()
    print(desc.money)
    print("우민규돈", desc.spend(300))
    
    print(desc.cnt_nuclear)
    print(desc.war())
    print(desc.war())
    print(desc.war())
    print(desc.war())
    print(desc.war())
    print(desc.war())