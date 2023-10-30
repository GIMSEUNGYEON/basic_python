#출력할 단수를 입력하세요
#구구단
a = input("출력할 단수를 입력하세요")

arr = range(1, 9+1)

for i in arr : 
    # print("{} * {} = {}".format(int(a), i, int(a)*i))
    print(a + "*" + str(i) + "=" + str(i*int(a)))