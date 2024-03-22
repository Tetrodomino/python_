import numpy as np

# 전치 연산
""" n × k 배열을 k × n 배열로 만들기 """
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.transpose()) # [[1 4] [2 5] [3 6]]

# transpose는 적용해도 a에 그대로 남지 않으므로 변경 상태로 남기고 싶으면 대입이 필요
"""
ex)
a.transpose()
print(a) ← transpose 되지 않은 a가 그대로 출력됨

a = a.transpose()
pirnt(a) ← 이래야 a가 전치된 상태로 출력
"""


# 배열 크기 변경
""" reshape(n, k) : 배열을 n × k의 크기로 바꾸기 
만약 k에 -1이 들어가면 n개의 행에 열 개수는 상관없는 크기의 배열이 됨

배열의 크기는 반드시 n × k의 값과 같거나
-1을 썼을 경우 n이나 k에 나누어 떨어져야 함"""

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a.reshape(5, -1)) # [[1 2] [3 4] [5 6] [7 8] [9 10]]


# flatten, rave1 : 2차원 이상의 배열을 1차원으로 만들기
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a.flatten()) # [1 2 3 4 5 6 7 8]

