# A + B를 정해진 횟수만큼 반복
T = int(input())
count = [];

for i in range(T):
    num = list(map(int, input().split())) # 배열로 입력받기
    count.append(num)

for i in count: # count의 항목 갯수 만큼 반복, i에는 count의 각 값이 대입됨
    print(i[0] + i[1])