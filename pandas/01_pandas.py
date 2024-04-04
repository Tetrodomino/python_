import pandas as pd

# 판다스는 기본적으로 넘파이와 비슷한 배열 기능을 제공하고
# 배열과 더불어 각 항목에 index 값 부여 가능
s = pd.Series([1, 2, 3, 4], index=['n1', 'n2', 'n3', 'n4'])
print(s)

