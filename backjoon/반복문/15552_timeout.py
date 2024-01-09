# 시간초과를 조심하기
# input()은 for 등으로 반복해서 실행하면 은근히 늘어지기 때문에
# 엄청난 횟수의 반복이 요구될 때는 sys.stdin.readline 을 사용해야 됨
import sys

T = int(input())

for i in range(T):
    a,b = map(int,sys.stdin.readline().split()) # 여러 수의 sys 입력받기
    print(a + b)