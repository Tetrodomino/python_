##### 문자열 인덱싱 #####
s = 'Life is too short, You need Python'

# 문자열을 하나의 배열처럼 생각해서 0번째부터 추출이 가능
a = s[0] # L
a = s[5] # i
print(a)

# -값을 넣으면 뒤에서부터 셈
a = s[-1] # n
a = s[-6] # P
print(a)


# string[a:b] 의 형식을 통해 문자열의 일부를 추출 가능, 이를 슬라이싱이라 함
# 이 때 string[b] '직전'까지의 문자를 추출함에 유의

a = s[0:4] # Life
a = s[-6:-1] # Pytho
print(a)

# 숫자를 생략하면 그 뒤나 앞 전체를 리턴

a = s[:] # s 전체 대입
a = s[:7] # Life is


# string[a] 에 값을 바로 대입하면 오류 발생, 문자열을 바꾸고 싶으면 자르고 이어붙이는 과정 필요
a = 'pithon'
# a[1] = y ← 오류 발생
a = a[:1] + 'y' + a[2:] # 이렇게 해야 변경 가능
print(a)