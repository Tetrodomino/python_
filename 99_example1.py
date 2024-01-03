# 두 숫자를 공백을 두고 입력해서 시간 입력하고 45분 앞당기기

a = -1
b = -1

while a < 0 or a > 23 or b < 0 or b > 59:
    a, b = map(int, input().split())

b = b - 45
if b < 0:
    a = a - 1
    b = b + 60

if a < 0:
    a = a + 24

print(a, b)