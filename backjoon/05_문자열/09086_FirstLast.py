# 문자열의 첫 글자와 마지막 글자
N = int(input())

for i in range(N):
    S = input()
    print(S[0] + S[len(S) - 1])