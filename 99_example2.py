a = -1
b = -1
c = -1

while a < 0 or a > 6 or b < 0 or b > 6 or c < 0 or c > 6:
    a, b, c = map(int, input().split())

coin = 0
situation = 0;

if a == b and a == c:
    coin = 10000 + 1000 * a

elif a != b and a != c and b != c:
    cost = 0;
    if a > b:
        if a > c:
            cost = a
        else:
            cost = c
    else: 
        if b > c:
            cost = b
        else:
            cost = c
    coin = cost * 100
else:
    if a == b:
        coin = 1000 + 100 * c
    elif b == c:
        coin = 1000 + 100 * a
    else:
        coin = 1000 + 100 * b

print(coin)