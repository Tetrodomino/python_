p = int(input())
g = 'F'

if p >= 60:
    g = 'D'
if p >= 70:
    g = 'C'
if p >= 80:
    g = 'B'
if p >= 90:
    g = 'A'

print(g)