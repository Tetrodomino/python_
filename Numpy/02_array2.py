import numpy as np

# 자료형
# 넘파이로 선언한 배열의 자료형을 확인하려면 dtype 메소드 사용
# 넘파이 배열은 리스트와 달리 선언할 때 정해진 하나의 자료형만 들어갈 수 있음

x = np.array([1, 2, 3])
print(x.dtype) # int 32

x = np.array([1.0, 2.0, 0.5])
print(x.dtype) # float 64

x = np.array([1, 2, 3.0]) # 3.0의 자료형인 float에 맞춰짐
print(x.dtype) # float 64 


# 배열을 선언할 때 dtype 인자를 지정함으로서 배열의 자료형 지정 가능
x = np.array([1, 2, 3], dtype='f')
print(x.dtype) # float 32

x = np.array([1, 2, 3], dtype='S')
print(x.dtype) # |S1
print(x[0] + x[1]) # '12'

"""
dtype 인자의 종류
b - boolean
i - integer
u - unsigned integer
f - float
O - object
S - byte String
U - unicode String

i나 f같은 크기를 가질 수 있는 자료형은 옆에 숫자를 붙임으로서 바이트 크기 설정 가능
ex) i8 (integer 8바이트) = int64
"""


# inf, nan
# 넘파이에서 계산할 때 무한대의 값이 나오면 inf, 정의할 수 없으면 nan이 나옴
x = np.array([0, 1, -1, 0]) / np.array([1, 0, 0, 0])  # 각각 계산한 배열 생성

print(x) # 0. / inf / -inf / nan



# 단순 배열 생성
""" zeros, ones 등이 있으며 단순한 형태의 배열을 만들 때 사용 """

# zeros(n) : n개의 0.0(실수) 값을 가진 배열 생성
a = np.zeros(5)
print(a) # [0. 0. 0. 0. 0.]
