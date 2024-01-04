import math
# 1002번 터렛 문제

# 시행 횟수
T = 0

# 결과 리스트
point = []

# 시행 횟수 입력
while T < 1:
    T = int(input())

# 시행 횟수에 따라 반복
for i in range(T):
    x1 = 10001
    y1 = 10001
    r1 = 10001
    x2 = 10001
    y2 = 10001
    r2 = 10001

    # 좌표와 반지름 입력
    while max(x1, x2, y1, y2, r1, r2) > 10000 or min(x1, x2, y1, y2) < -10000 or min(r1, r2) < 1:
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 좌표(x1, y1), (x2, y2) 사이의 거리 구하기
    d1 = x1 - x2
    d2 = y1 - y2
    d1 = math.pow(d1, 2)
    d2 = math.pow(d2, 2)
    distance = math.sqrt(d1 + d2)

    # 반지름 큰 순서대로 정렬 (어차피 뒤바꿔도 결과 변화 X)
    if r1 < r2:
        temp = r1
        r1 = r2
        r2 = temp

    # 두 원 사이의 교차점이 조건에 맞는 가능한 위치이므로 이를 구하는 로직
    # 1. 두 점의 위치가 같지 않을 경우
    if distance != 0:
        # 만약 반지름이 두 점 사이의 거리보다 클 경우 구하기
        if r1 > distance or r2 > distance:
            if r2 + distance > r1:      # [작은 원의 반지름] + [거리] 합이 큰 원의 반지름보다 크면 교차점 2개
                point.append(2)
            elif r2 + distance == r1:   # [작은 원의 반지름] + [거리] 합이 큰 원의 반지름보다 같으면 1개
                point.append(1)
            else:                       # 큰 원이 작은 원을 완전히 포함하고 있으면 0개
                point.append(0)
        # 만약 반지름이 두 점 사이의 거리보다 작을 경우
        else:
            if r1 + r2 > distance:      # 두 반지름의 합이 거리보다 크면 교차점 2개
                point.append(2)
            elif r1 + r2 == distance:   # 같으면 교차점 1개
                point.append(1)
            else:                       # 거리보다 작은 원이면 아예 겹치지 않으므로 0개
                point.append(0)
    # 2. 두 점의 위치가 같을 경우
    else:
        if r1 == r2:            # 반지름이 같으면 완전히 같은 원이므로 무한대(-1)
            point.append(-1)
        else:                   # 반지름이 같지 않으면 교차점이 생길 수 없으므로 0
            point.append(0)

# 결과 출력
for i in range(len(point)):
    print(point[i])