# N + 1년이 N년의 요소로 나누어떨어지는 경우 찾기
N = int(input())

for i in range(N):
    Y = input()
    K = int(Y) + 1
    Z = int(Y[2:4])
    if K % Z == 0:
        print('Good')
    else:
        print('Bye')

