# 내장 함수 2

# hex
""" 정수를 입력받아 16진수 문자열로 변환하여 리턴 """
print('──────────hex──────────')
print(hex(14)) # 0xe


# id
""" 아무 자료형이나 오브젝트를 입력받아 해당 오브젝트의 주솟값(레퍼런스) 반환 """
print('──────────id──────────')
a = 1
print(id(3))
print(id(a))


# input
""" 엔터를 기준으로 입력을 받는 함수
입력받은 문자열은 프롬프트가 됨 """
print('──────────input──────────')
#print(input()) # 입력한 문자열
print('input 실행')


# int
""" 문자열 형태의 수나 소숫점이 있는 실수를 정수로 바꾸는 함수(소숫점은 버림)
정수가 입력되면 그대로 리턴 """
print('──────────int──────────')
print(int('3')) # 3
print(int(4.81231)) # 4


# isinstance
""" 첫 번째 인수는 객체, 두 번째 인수는 클래스 필요
입력한 객체가 해당 클래스의 인스턴스(선언된 클래스)면 True, 아니면 False 리턴 """
print('──────────isinstance──────────')
class Person: pass
a = Person()
b = 0
print(isinstance(a, Person)) # True
print(isinstance(b, Person)) # False


# len
""" 문자열의 길이나 리스트, 튜플의 요소 개수를 리턴 """
print('──────────len──────────')
print(len((1, 2, 3, 4))) # 4
print(len("abcdefg")) # 7


# map
""" 첫 번째 인수는 함수, 두 번째 인수는 반복 가능한 데이터(리스트, 튜플 등) 필요
입력받은 데이터의 각 요소에 첫 번째 인수로 넣은 함수를 적용한 결과를 리턴"""
print('──────────map──────────')
def mul_two(num):
    return num * 2

print(list(map(mul_two, [1, 2, 3, 4]))) # [2, 4, 6, 8]
print(list(map(int, '2 3 4 5'.split()))) # [2, 3, 4, 5]


# pow(x, y)
""" x의 y제곱 """
print('──────────pow──────────')
print(pow(2, 3)) # 8
print(pow(3, 2)) # 9



# range
""" 입력받은 숫자에 해당하는 정수 리스트를 만들기"""
print('──────────range──────────')

# 인수가 하나일 경우
""" 0부터 시작하여 인수-1 까지 """
print(list(range(5))) # [0, 1, 2, 3, 4]

# 인수가 2개일 경우
""" 첫 번째 인수부터 시작하여 2번째 인수-1 까지 """
print(list(range(2, 7))) # [2, 3, 4, 5, 6]

# 인수가 3개일 경우
""" 1번째 인수부터 2번째 인수-1 까지 3번째 인수의 간격대로 """
print(list(range(2, 11, 2))) # [2, 4, 6, 8, 10]



# round
""" 소숫점이 있는 숫자를 반올림 """
print('──────────round──────────')
print(round(5.4212)) # 5
print(round(5.482, 2)) # 5.48 - 2번째 인수는 반올림해서 나타낼 자릿수의 위치



# sorted
""" 리스트나 문자열, 튜플을 정렬하고 리스트로 리턴 """
print('──────────sorted──────────')
print(sorted([3, 2, 7])) # [2, 3, 7]
print(sorted("apple")) # ['a', 'e', 'l', 'p', 'p']
print(sorted((2, 8, 4, 23))) # [2, 4, 8, 23]
