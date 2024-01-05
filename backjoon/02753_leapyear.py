y = int(input())
c = 0
if y % 4 == 0:
    c = 1
if y % 100 == 0:
    c = 0
if y % 400 == 0:
    c = 1

print(c)