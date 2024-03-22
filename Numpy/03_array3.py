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



# 배열 연결
""" hstack([a, b]) : 행의 수가 같은 a와 b를 옆으로 연결하여 열을 늘림 """
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6, 7] ,[8, 9, 10]])
print(np.hstack([a, b])) # [[1 2 5 6 7] [3 4 8 9 10]]

""" vstack([a, b]) : 열의 수가 같은 a, b를 세로로 연결하여 행을 늘림 """
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8] ,[9, 10]])
print(np.vstack([a, b])) # [[1 2] [3 4] [5 6] [7 8] [9 10]]

""" dstack([a, b]) : 크기(shape)가 같은 배열끼리만 실행 가능하며 깊이 방향으로 합침 """
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dstack([a, b])) #[[[1 4] [2 5] [3 6]]] - 1 x 3 x 2 배열이 됨

""" stack([a, b]) : 역시 크기가 같은 배열끼리만 실행 가능하며 axis 값에 따라 배열을 연결(기본값 0)
axis 0이면 a를 평평한 판에 깔고 b를 아래에 두는 식으로 추가한다고 보면 되며
1이면 다른 방향으로 배열을 자르고 붙임
https://everyday-image-processing.tistory.com/87
"""

""" r_([a, b]) : 
"""