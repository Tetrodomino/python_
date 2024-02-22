# 바구니에 공 넣기
N, M = map(int, input().split())

basket = []
for i in range(N):
    basket.append(0)

for i in range(M):
    a, b, c = map(int, input().split())
    for k in range(a - 1, b):
        basket[k] = c

for i in range(len(basket)):
    print(basket[i], end=" ")