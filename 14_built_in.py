# 내장 함수 Built-in function
""" 별도 import 없이 바로 사용할 수 있는 함수 """

# abs
""" 수의 절댓값을 구하기 """
print('────────abs─────────')
print(abs(-3)) # 3
print(abs(1.2)) # 1.2



# all
""" 반복 가능한 변수(리스트, 튜플, 문자열, 딕셔너리 등)를 받아
모두 참이면 True, 하나라도 거짓(정수/실수면 0, 문자열이면 빈 문자열)이면 False 반환 """
print('─────────all────────')
print(all([1, 2, 3])) # True
print(all((-1, 1, 1))) # True
print(all('aasdffa')) # True
print(all([0, 1, 2])) # 0이 있으므로 False
print(all([])) # 빈 값은 True 리턴



# any
""" all과 비슷하게 반복 가능한 변수를 받아
하나라도 참이면 True, 모두 거짓이면 False 반환 """
print('─────────any────────')
print(any([0, 0, 1])) # True
print(any('')) # 빈 문자열은 False
print(any([])) # 빈 값은 False


# chr
""" 숫자를 입력받아 거기에 해당하는 유니코드 문자를 반환 """
print('─────────chr────────')
print(chr(97)) # a
print(chr(44032)) # 가


# ord
""" 유니코드 문자를 입력받아 거기에 해당하는 수를 반환 """
print('─────────ord────────')
print(ord('각')) # 44033
print(ord('ㄱ')) # 12593


# dir
""" 특정 객체가 지닌 함수나 메서드를 보여주는 함수"""
print('─────────dir────────')
# 1. 리스트
print(dir([1])) # append, count, clear, copy, insert ...
# 2. 튜플
print(dir(())) # count, index ...


# divmod
""" 두 개의 숫자를 입력받아 a ÷ b의 몫과 나머지를 튜플로 반환 """
print('─────────divmod────────')
print(divmod(1, 2)) # (0, 1)
print(divmod(13123, 59)) # (222, 25)


# enumerate
""" 열거. 순서가 있는 데이터(리스트, 튜플, 문자열 등)를 입력받아
index 순서를 붙인 enumerate 객체로 리턴
보통 for와 같이 사용 """
print('────────enumerate─────────')
for i, name in enumerate(['a', 'b', 'd']):
    print(i, name)
# 출력결과
"""
0 a
1 b
2 d
"""


# eval
""" 문자열로 구성된 표현식을 입력받아 문자열이 아닐 때 실행값을 리턴하는 함수 """
print('─────────eval────────')
print(eval('1 + 2')) # 3
print(eval('2')) # 2
print(eval('divmod(3,2)')) # (1, 1)


# filter
""" 첫 번째 인수에는 리턴이 boolean인 함수, 두 번째 인수에는 반복 가능한 데이터 필요
두 번째 인수에 들어간 데이터의 요소를 함수에 하나씩 넣어서 리턴값이 True인 것만 묶어서 리턴 """
print('─────────filter────────')
def ten(x):
    return x > 10

# filter의 반환값은 포인터(레퍼런스)의 형식만 나오므로 list나 tuple 등으로 형식 지정이 필요
print(list(filter(ten, [12, 6, 7, 35, 2, 0]))) # [12, 35]
print(tuple(filter(ten, (7, 8, 9, 10, 11, 12)))) # (11, 12)

