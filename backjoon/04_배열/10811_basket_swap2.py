# 바구니 뒤집기
N, M = map(int, input().split())

basket = []
for i in range(N):
    basket.append(i + 1)

for i in range(M):
    a, b = map(int, input().split())

    k = 0
    for i in range(a - 1, b):
        if i >= b - k - 1:
            break

        temp = basket[i]
        basket[i] = basket[b - k - 1]
        basket[b - k - 1] = temp
        k = k + 1

for i in range(len(basket)):
    print(basket[i], end=" ")