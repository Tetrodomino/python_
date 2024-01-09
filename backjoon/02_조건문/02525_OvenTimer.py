# 오븐 시계
# 첫 줄에는 현재 시각, 두 번째 줄에는 조리 시간을 입력하여 요리가 완료되는 시각 구하기

a, b = map(int, input().split())
t = int(input())

b += t
a += int(b / 60)
b %= 60

if a > 23:
    a -= 24

print(a, b)