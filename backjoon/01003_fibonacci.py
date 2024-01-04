# 피보나치 수 구하기 (더하기로만 하기)
T = int(input())
count = [];

# 반복 횟수 입력 
for i in range(T):
    K = int(input())
    count.append(K)

for i in count: # count의 항목 갯수 만큼 반복, i에는 count의 각 값이 대입됨
    t = 0
    result = [1, 0]

    # 1번째 값을 2번째에 더하고 기존 2번째 값은 1번째에 대입
    for i in range(i):
        t = result[1]
        result[1] += result[0]
        result[0] = t

    print(result[0], result[1])