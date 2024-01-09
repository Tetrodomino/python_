# A + B 1번, 1001번 문제도 똑같음
a = -1
b = 11
while a <= 0 or b >= 10:
    a, b = map(int, input().split())

print(a + b)