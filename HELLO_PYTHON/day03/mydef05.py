def add_min_mul_div(a, b):
    return a + b, a - b, a * b, a / b

sum, min, mul, div = add_min_mul_div(4, 2)
# return개수와 받는 변수의 개수가 같아야함
# 근데 받는 변수가 1개라면 튜플로 받음(배열과는 비슷하지만 다름)(소괄호 이용)(인덱스는 배열과 똑같이 가짐)

print(f"sum : {sum}")
print(f"min : {min}")
print(f"mul : {mul}")
print(f"div : {div}")
