# 바이트에 따른 long 개수(4바이트당 1개) 늘리기
X = int(input())
Y = ''

for i in range(int(X/4)): # 4로 나누면 자료형이 float이 되므로 int로 변환시켜야 함
    Y += 'long '

Y += 'int'

print(Y)