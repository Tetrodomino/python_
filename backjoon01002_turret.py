import math

T = 0
point = []
while T < 1:
    T = int(input())

for i in range(T):
    x1 = 10001
    y1 = 10001
    r1 = 10001
    x2 = 10001
    y2 = 10001
    r2 = 10001

    while max(x1, x2, y1, y2, r1, r2) > 10000 or min(x1, x2, y1, y2) < -10000 or min(r1, r2) < 1:
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d1 = x1 - x2
    d2 = y1 - y2
    d1 = math.pow(d1, 2)
    d2 = math.pow(d2, 2)
    distance = math.sqrt(d1 + d2)

    if r1 < r2:
        temp = r1
        r1 = r2
        r2 = temp

    if distance != 0:
        if r1 > distance or r2 > distance:
            if r2 + distance > r1:
                point.append(2)
            elif r2 + distance == r1:
                point.append(1)
            else:
                point.append(0)
        else:   
            if r1 + r2 > distance:
                point.append(2)
            elif r1 + r2 == distance:
                point.append(1)
            else:
                point.append(0)
    else:
        if r1 == r2:
            point.append(-1)
        else:
            point.append(0)

for i in range(len(point)):
    print(point[i])