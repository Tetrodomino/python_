# A B C 식의 나머지 구하기
a, b, c = map(int, input().split())

print((a + b) % c)
print((a % c + b % c) % c)
print((a * b) % c)
print((a % c * b % c) % c)