# 두 수 비교하기
a, b = map(int, input().split())

s = ''
if a == b:
    s = '=='
else:
    s = '>' if a > b else '<'

print(s)