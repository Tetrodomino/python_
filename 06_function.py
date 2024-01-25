# 함수
"""
def 함수이름(매개변수):
    실행문
"""
# 위와 같은 방식으로 작성


# 리턴값이 필요할 경우 return 작성
def add(a, b): # a, b 를 매개변수(parameter)라고 함
    return a + b

print(add(3, 4)) # 실제 함수를 사용할 때 매개변수 자리에 넣는 3, 4 같은 값을 인수(argument)라고 함



# 매개변수 지정
def sub(a, b):
    return a - b;

print(sub(b = 7, a = 9)) # 이런 식으로 지정하면 인수의 순서를 바꿔서도 사용 가능



# 입력값이 여러 개인 함수

def add_tuple(*a):  # *a 식으로 쓰면 입력한 모든 변수를 튜플로 만들어서 사용
    k = 0
    for n in a:
       k += n
    return k
    
print(add_tuple(1, 2, 3, 4, 5, 6))


def add_dictionary(**a): # **a 식으로 쓰면 입력한 매개변수를 딕셔너리 형태로 만들어서 사용
    print(a)

add_dictionary(a=1, b=2, c=3) # a, b, c의 키를 가진 딕셔너리가 됨



# 튜플형 리턴값
def add_mult(a, b):
    return a + b, a * b # 리턴값이 두 개가 되는 것이 아닌 두 리턴값을 하나의 튜플로 만들어서 리턴

print(add_mult(3, 4)) # 튜플로 a + b, a * b가 출력됨 (7, 12)



# 초기값이 설정된 매개변수
def add_3(a, b, c = 0):
    return a + b + c

print(add_3(3, 4)) # a, b의 매개변수만 적용되어 7
print(add_3(5, 4, 5)) # c에 값이 적용되므로 14



# lambda 예약어
# def 와 동일한 역할을 하지만 간결하게 표현 가능
"""
함수이름 = lambda 매개변수: 반환값 생성문
"""
add_lambda = lambda a, b: a + b
print(add_lambda(1, 2)) # 3