# 공 바꾸기
N, M = map(int, input().split())

basket = []
for i in range(N):
    basket.append(i + 1)

for i in range(M):
    a, b = map(int, input().split())
    temp = basket[a - 1]
    basket[a - 1] = basket[b - 1]
    basket[b - 1] = temp

for i in range(len(basket)):
    print(basket[i], end=" ")