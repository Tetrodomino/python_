# 별 찍기 1
S = int(input())

for i in range(S):
    star = '*'
    for j in range(i):
        star += '*'
    print(star)