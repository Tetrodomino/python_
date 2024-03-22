# 공 바꾸기
N, M = map(int, input().split())

basket = []
for i in range(N):
    basket.append(i + 1)

for i in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue

    c = round((b - a) / 2.0)
    print(c)

    for k in range(c):
        temp = basket[a + k]
        basket[a + k] = basket[b - k]
        basket[b - k] = temp

    for i in range(len(basket)):
        print(basket[i], end=" ")


for i in range(len(basket)):
    print(basket[i], end=" ")