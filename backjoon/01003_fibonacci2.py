# 원래 피보나치를 구하는 방식
T = int(input())
count = [];

for i in range(T):
    K = int(input())
    count.append(K)

for i in count:
    cond = True

    temp = [i]
    result = [0, 0]

    while cond:
        if temp[0] <= 1:
            cond = False

        temp2 = []

        for k in range(len(temp)):
            if temp[k] > 3:
                temp2.append(temp[k] - 2)
                temp2.append(temp[k] - 3)
                temp2.append(temp[k] - 3)
                temp2.append(temp[k] - 4)
            elif temp[k] > 1:
                temp2.append(temp[k] - 1)
                temp2.append(temp[k] - 2)
            elif temp[k] == 1:
                result[1] += 1
            else:
               result[0] += 1
        temp = temp2

    print(result[0], result[1])