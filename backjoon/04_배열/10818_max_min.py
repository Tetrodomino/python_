# 배열 내 최댓값과 최솟값

N = int(input())

a = list(map(int, input().split()))

max = -1000001
min = 1000001

for i in range(N):
    max = a[i] if a[i] > max else max
    min = a[i] if a[i] < min else min

print(min, max)