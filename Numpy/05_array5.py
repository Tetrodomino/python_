import numpy as np
# 배열 통계

# len(x) : x의 요소 개수
x = np.array([1, 2, 3, 4, 5])
print(len(x)) # 5

# var(x) : x의 분산(각 항목 평균차의 제곱평균)
print(np.var(x)) # 2

# std(x) : x의 표준편차
print(np.std(x)) # 1.4142...

# max(x), min(x) : x의 최대, 최소

# percentile(x, n) : x의 값을 정렬했을 때 n/100 위치에 있는 값
# 가령 percentile(x, 25)일 경우 x의 값 중 가장 작은 것에서부터 25% 위치의 값이 나오고
# percentile(x, 100) 일 경우 최댓값이 나옴
print(np.percentile(x, 25)) # 2