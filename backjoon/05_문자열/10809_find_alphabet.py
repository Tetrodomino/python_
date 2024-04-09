# 알파벳 찾기
S = input()

alpha = []
for i in range(26):
    alpha.append(-1)

for i in range(len(S)):
    k = ord(S[i]) - 97
    if alpha[k] != -1:
        continue
    alpha[k] = i

for i in range(26):
    print(alpha[i], end=" ")
