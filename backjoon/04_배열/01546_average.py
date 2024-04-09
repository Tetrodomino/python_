# 점수 평균 구하기
N = int(input())

point = []
point = list(map(int, input().split()))

pointsum = 0
highscore = 0

for i in range(N):
    if point[i] > highscore:
        highscore = point[i]

for i in range(N):
    point[i] = point[i] / highscore * 100.0
    pointsum += point[i]

print(pointsum / N)