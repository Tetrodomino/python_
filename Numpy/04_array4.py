import numpy as np

# 배열 연산

""" + : 각 요소를 더하기 """
x = np.arange(1, 1001) # 1 ~ 1000
y = np.arange(1001, 2001) # 1001 ~ 2000

z = x + y # 그냥 연산이 가능, for를 이용하는 것보다 이것이 훨씬 연산이 더 빠름
print(z[:10]) # 1002, 1004, 1006, 1008 ...

""" == : 각 요소를 비교하여 같으면 True, 다르면 False를 각각 리턴 """
a = np.array([1, 2, 3, 4])
b = np.array([1, 3, 2, 4])
print(a == b) # [True False False True]

""" >, <, >=, <= : 각 요소의 대소관계를 비교하여 조건 만족 시 True, 다르면 False를 각각 리턴 """
print(a >= b) # [True False True True]

""" all : 모든 요소를 비교하여 조건을 만족하면 True, 하나라도 만족하지 못하면 False """
print(np.all(a == b)) # False
print(np.all(a == np.array([1, 2, 3, 4]))) # True

""" 그 외 연산들은 각각의 요소에 대해 작동 """
print(a + 1) # [2 3 4 5]
print(np.exp(a)) # [e, e^2, e^3, e^4]
print(a * 10) # [10 20 30 40]



# 정렬
""" sort를 사용
np.sort(a) : a를 정렬

인수로는 axis가 있음
axis = -1 (default) : 가장 안쪽의 값만 정렬
axis = 0 : 행 정렬
axis = 1 : 열 정렬
"""
a = np.array([[4, 3, 5, 7], [1, 12, 11, 9], [2, 15, 1, 14]])

print(np.sort(a)) # [[3 4 5 7] [1 9 11 12] [1 2 14 15]] 가장 하위 요소를 정렬

print(np.sort(a, axis=0)) # [[1 3 1 7] [2 12 5 9] [4 15 11 14]]
"""
[
[1 3  1  7 ]
[2 12 5  9 ]
[4 15 11 14]
]
이렇게 세로를 기준으로 정렬
"""

print(np.sort(a, axis=1)) # [[3 4 5 7] [1 9 11 12] [1 2 14 15]] 열을 기준으로 정렬



# 기타 연산, 배열의 특정 연산
x = np.array([1, 2, 3, 4])

# 최대, 최소
"""
min : 최솟값
max : 최댓값
argmin : 최솟값의 위치
argmax : 최댓값의 위치
"""
print(np.min(x), np.max(x), np.argmin(x), np.argmax(x)) # 1 4 0 3

# 통계
"""
sum : 총합
mean : 평균(float64)
median : 중앙값(float64), 만약 배열 내 요소의 개수가 짝수일 경우 중앙에 있는 두 개 값의 평균을 리턴
"""

