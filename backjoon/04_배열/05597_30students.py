# 30명의 학생 중 과제를 내지 않은 학생 찾기

stu = []
for i in range(30):
    stu.append(0)

for i in range(28):
    a = int(input())
    stu[a - 1] = 1

for i in range(30):
    if stu[i] == 0:
        print(i + 1)