arr = ["홍길동", "전우치"]
brr = ['ping', 'pong']
print(arr)
# 자바스크립트와 유사하게 가변 배열기능을 지원함. 객체 자체의 값이 아닌 

arr.append("허균")
print(arr)

arr.insert(len(arr), "유관순")
print(arr)

arr.append(brr)
print(arr)
# 배열 자체를 객체로 배열에 넣는다

arr.extend(brr)
print(arr)
# 다른 배열의 요소들을 배열에 그대로 넣는다

