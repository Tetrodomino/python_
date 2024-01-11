S = int(input())

for i in range(S):
    star = ''
    for j in range(S):
        if j +2 > S - i:
            star += '*'
        else:
            star += ' '
    print(star)