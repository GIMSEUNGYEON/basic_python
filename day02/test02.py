# 첫 수를 입력하세요
# 두번째 수를 입력하세요.
# 3과 6의 합은 9입니다.

a = input("첫번째 수를 입력하세요")
b = input("두번째 수를 입력하세요")

# print(a, "와 ", b, "의 합은 ", int(str(a)) + int(str(b)), "입니다.") 
print(a + "와 " +  b + "의 합은 " + str(int(a) + int(b)) + "입니다.") 

# 타입이 같으면(str) +로 문자열을 연결할 수 있는데 
# int타입은 + 연산으로 문자열 연결이 불가능하다. str타입으로 캐스팅해주거나 ,로 붙이거나

print("{}과 {}의 합은 {}입니다.".format(a,b,int(a)+int(b)))
#아님 이렇게 쓰거나.... printf같네....