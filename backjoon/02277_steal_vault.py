# 금고의 번호를 모두 동일한 값으로 맞추기
import random

# a, b를 더할 때 숫자의 갯수인 M 이상이 되면 오버플로우처럼 M보다 작은 값으로 돌리기
def add1(a, b, M):
    if a+b >= M:
        return a + b - M
    elif a + b < 0:
        return a + b + M
    else:
        return a + b

# a, b 두 값의 거리를 구하기, a가 기준점이고, b는 비교할 지점
# a의 값을 기준으로 올라가는 쪽이 더 b와 가까우면 양수, 내려가는 쪽이 더 가까우면 음수 리턴
def get_distance(a, b, M):
    if a == b:
        return 0

    if a > b: # a가 b보다 크면 가상의 윗점인 c는 M을 더함
        c = b + M
        if c - a >= a - b: # 내려가는 것이 더 가까우면 음수
            return b - a
        else:
            return c - a
    else: 
        c = b - M
        if b - a >= a - c: # 내려가는 것이 더 가까우면 음수
            return c - a
        else:
            return b - a
        
# N은 A의 초기 항목 수, M은 각 항목의 최대값
N, M = map(int, input().split())

# N의 개수만큼 각 번호 입력
#A = list(map(int, input().split()))
A = random.choices(range(0, M), k=N)
print(A)

Time = 0

# 시간 구하는 로직
"""
1. 하나의 지점을 기준으로, 해당 지점의 왼쪽의 거리와 오른쪽 거리의 부호가 다르면 이 상태임
ㅇ
  ㅇ
    ㅇ
또는
    ㅇ
  ㅇ
ㅇ
이 경우 지점의 위치를 변경하지 않고 그냥 넘어감

2. 만약 부호가 같으면 아래와 같은 상태
ㅇ  ㅇ
  ㅇ
또는
  ㅇ
ㅇ  ㅇ
이 경우 해당 지점의 위치를 왼쪽이나 오른쪽 중 더 가까운 곳으로 옮기고 그만큼 시간에 더한 다음 해당 지점을 제거
"""

while len(A) > 1:
    # 항목이 두 개만 남으면 차이만큼의 시간만 더 필요하므로 계산하고 바로 종료
    if len(A) == 2:
        Time += abs(A[0] - A[1])
        break

    for i in range(len(A)):
        if i == 0 and A[-1] == A[0]: # 0번째 위치는 -1번째 위치랑 같이 이동할 수 없으므로 두 항목이 같을 경우 비교하지 않고 넘어감
            continue

        if i > 0 and A[i] == A[i-1]: # 초기에 설정된 값 중 같은 값이 있으면 하나를 없애고 재실행
            del A[i]
            break

        left = get_distance(A[i], A[i-1], M)
        right = 0
        if i < len(A) - 1:
            right = get_distance(A[i], A[i+1], M)
        else:
            right = get_distance(A[i], A[0], M)
        print(left, right)
        print(A)

        if left * right < 0: # 두 거리의 부호가 다르면 곱할 때 음수만 나옴
            continue
        else:
            l = abs(left)
            r = abs(right)
            if l > r:
                Time += r
                del A[i]
            elif l == r:
                Time += r
                del A[i]
                del A[i+1]
            else:
                Time += l
                del A[i]
            break

print(Time)
