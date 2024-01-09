a = int(input())
b = int(input())

b_3 = b % 10
b_2 = int((b - b_3) % 100 / 10)
b_1 = int((b - b_3 - b_2 * 10) / 100)

print(a * b_3)
print(a * b_2)
print(a * b_1)
print(a * b)