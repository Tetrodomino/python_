# 영수증 검사
X = int(input())
Y = int(input())
Z = 0

for i in range(Y):
    a, b = map(int, input().split())

    Z += a * b

p = 'Yes' if X == Z else 'No'
print(p)