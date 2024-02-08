# 다리를 놓는 수 구하기
"""
M개의 우측 사이트에서 N개의 사이트를 고를 때
하나의 다리라도 교차되는 일이 없다면 순서가 항상 정해져있어야 하므로 조합의 방식이 적용
"""
import math

T = int(input())

for i in range(T):
    a, b =  map(int, input().split())
    print(math.comb(b, a))