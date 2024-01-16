##### 문자열 자료형 #####

# 문자열을 만드는 4가지 방법
# 1. '' 사용
s1 = 'Hi!'

# 2. "" 사용
s2 = " my name"

# 3. ''' ''' 사용 (작은 따옴표 3개)
s3 = ''' is My!'''

# 4. """ """ 사용 (큰 따옴표 3개)
s4 = """ and you?"""

print(s1, s2, s3, s4)


# 따옴표를 포함시키고 싶으면 아래와 같은 방법 존재
# 1. '' 안에 " 사용
# 2. "" 안에 ' 사용
# 3. 표현하고자 하는 따옴표 옆에 \ 붙이기
say1 = 'samsung say "we are best"'
say2 = "apple's samsung"
say3 = 'No, samsung\'s not apple\'s'


# 줄바꿈 하는 법
# 1. 이스케이프 코드 \n 사용
# ''' ''' 이나 """ """ 사용
st1 = 'yeeeeeee\neeeeeeees'
st2 = '''abcdefg
hijklmnop
qrstuvwxyz
'''

print(st1, st2)

##### 문자열 연산 #####

# + : 문자열을 이어붙인다
print("a" + 'b')
a = 'abc'
b = "def"
print(a + b)

# * : 문자열을 반복시킨다
s1 = 'long line!'
print('─' * 20)
print(s1*3)
print("-"*20)

# len(s) : 문자열의 길이를 구한다 (공백 포함)
print(len(s1))