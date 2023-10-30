print('hello world!!!!!')

a = 100

print(f'answer = {a}')

name = '김승연'

print(f'name = {name}')

print('test1 : {0}, test2 : {1}, test3 : {0}'.format('index0', 'index1','index2'))
#           index0        index1        index0                            안쓰임

print('중괄호를 입력하고 싶을때 {{}}, {}'.format('test'))

print('뒤에 포맷 인자가 없으면 {{}}가 그대로 나옴')

print('{0:<10} | {1:<5}'.format('10자리', '5자리'))
#왼쪽 정렬
print('{0:>8} | {1:>4}'.format('8자리', '4자리'))
#오른쪽 정렬
print('{0:^7} | {1:^9} | '.format('7자리', '9자리'))
#가운데 정렬 

# 정렬의 빈자리 채우기
print('{0:-^7} | {1:ㄱ^9} | '.format('7자리', '9자리'))
# ^<> 바로 앞에 채울 문자 입력

print('|{:^8}|{:>9}|'.format('test', 'test2'))
#인덱스 안써도 되네

print(f'|{name:^7}|')
