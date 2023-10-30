class Animal:

    def named(self, name):
        self.name = name


ani1 = Animal() # new 생략
ani1.named('멍멍이')

name1 = ani1.name

print('name : ' + name1)


class Animal2 : 
    def __init__(self):
        print('생성자1')
        self.name = ''
    def named(self, name):
        self.name = name
    def __str__(self):
        return "[Animal][name] : " + self.name
    def __del__(self):
        print('소멸자1')
        
class human(Animal2) : 
    def __init__(self):
        super().__init__()
        self.asset = 0
        print('생성자2')
    def goldspoon(self):
        self.asset = 10000000000
    def __str__(self):
        return "name : " + self.name + "\rasset : " + str(self.asset)    
    def __del__(self):
        print('소멸자2')

if __name__ == '__main__':
    ani2 = Animal2()
    
    # print("ani2.name : ",ani2.name)
    print(ani2)
    
    ani2.named('멍멍이')
    # print("ani2.name : ",ani2.name)
    print(ani2)
    
    print()
    
    hum = human()
    print(hum)
    print()
    hum.named('홍길동')
    print(hum)
    print()
    hum.goldspoon()
    print(hum)
    print()
    
    