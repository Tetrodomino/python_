# 앞에 Case를 붙여서 A + B 출력하기

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print("Case #%d: %d" % (i + 1, a + b))