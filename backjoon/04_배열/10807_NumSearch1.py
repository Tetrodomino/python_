# 배열 내 숫자가 몇 개인지 찾기

N = int(input())

a = list(map(int, input().split()))
c = 0
k = int(input())
for i in range(N):
    if a[i] == k:
        c += 1
    
print(c)