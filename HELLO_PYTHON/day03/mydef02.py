def showDan(dan):
    result = ""
    for i in range(1,9+1):
        result += f'{dan} * {i} = {str(dan * i)}\r'

    return result

print(showDan(3))

#////////////////////////////////////////////////////////////////////////

def showDan2(dan):
    for x in range(1, 9+1) :
        print(f"{dan} * {x} = {dan * x}")

showDan2(4)
# 파라미터 3은 문자형