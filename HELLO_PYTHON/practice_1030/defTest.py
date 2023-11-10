# 메서드에는 파라미터가 없는경우/1개인 경우/여러개인 경우, 
# 리턴값이 없는경우/1개인 경우/여러개인 경우로 조합하여 총 9가지 경우의 수가 있다.


# 파라미터가 없고, 리턴값도 없는 경우
def test1(): 
    print("hello!")


# 리턴값은 없지만 print가 있어 def를 호출한 경우 print가 자동 출력된다
# 리턴값 없는 def가 대부분 이렇게 생겼으니 리턴값이 없는 경우는 그만 살펴본다
test1()


# 파라미터가 없고, 리턴값은 있는 경우
def test2():
    return("hi!")


# 리턴값이 있지만 def 자체적으로 print를 못하므로 호출과 동시에 print를 해주거나
# 변수에 리턴값을 받아 저장할 수 있다.
print(test2())
sayHi = test2()
print(sayHi)


# 파라미터가 있고, 리턴값이 한개인 경우
def test3(a):
    return a * 3


# def 내에서 계산을 끝내는 형태
print(test3(5))


# 파라미터가 여러개고, 리턴값이 한개인 경우
def test4(a, b):
    return a + b


print(test4(5, 8))


# 파라미터가 여러개고, 리턴값도 여러개인 경우
def test5(a, b):
    return a + b, a - b, a * b, a / b


# 이런 경우 def의 리턴값을 받아 저장하는 변수는 하나이거나 
# 리턴값의 개수와 같은 개수의 변수가 값을 받아 저장해야한다.
tuple1 = test5(2, 4)
print(f"tuple1 : {tuple1}")
# 리턴값을 받아 저장하는 변수가 하나인 경우, 튜플 타입으로 저장된다.
# 튜플 타입 : 리스트와 거의 유사한 역할을 하는 배열의 일종으로, 리스트는 대괄호[]로 묶이지만 튜플은 소괄호()로 묶어 구분한다.
# 이외에도 튜플은 요솟값을 변경시킬 수 없고 선언할 때 괄호를 생략하는 차이가 있다.

plus, minus, multiply, divide = test5(2, 4)
# 리턴값을 받아 저장하는 변수가 리턴값의 개수와 같다. 1개거나 4개가 아닌 변수에 저장하려고 하면 오류가 발생함.
print(f"plus : {plus}")
print(f"minus : {minus}")
print(f"multiply : {multiply}")
print(f"divide : {divide}")


# 파라미터가 몇개가 들어올지 모르는 경우
def test6(*args):
    result = 0
    for i in args: 
        result += i
        # 파라미터로 들어오는 값을 모두 더한다
    return result


print(test6(1, 2))
print(test6(1, 2, 3, 4))


# 자바의 Map객체와 유사한 저장방법
def test7(**kwargs):
    print(kwargs)


test7(name='멍멍이', age=6)
# name, age : key 
# 멍멍이, 6 : value


# 파라미터 초깃값을 미리 설정하기
def test8(age, name='홍길동', human=True):
# 디폴트 값이 있는 변수는 디폴트 값이 없는 변수 뒤로 갈 수 없다. 호출할 때 파라미터를 넣어주는 순서 때문
    print('나의 이름은 %s입니다.' % name)
    print('나이는 %d살입니다.' % age)
    
    if human: 
        print("사람입니다.")
    else: 
        print("멍멍입니다.")

        
test8(4, '바둑이', False)

test8(25)  # 기본값이 들어간다

