# 기본 출력
print('Hello World!')

# 변수 출력
a = 1
print(a) # 1

# 식 출력 가능
b = 5
print(a + b) # 6

# 문자열 더하기 가능
a = '가나다'
b = '라마바'
print(a + b) # 가나다라마바

# 쉼표를 넣을 경우 띄워서 출력됨
print(a, b) # 가나다 라마바

# print마다 줄바꿈을 하지 않으려면 end 사용
# end 안의 값이 print마다 사이에 들어갈 문자열이 됨
for i in range(10):
    print(i, end=' ') # 0 1 2 3 4 5 6 7 8 9

# 문자열 안에 매개변수 넣기 (포매팅)
a = 2
b = 3
i = 1
print("Case #%d: %d + %d = %d" % (i + 1, a, b, a + b)) # Case #1: 2 + 3 = 5
