# (4) 문자열 포매팅
# 문자열 사이에 다른 변수의 값을 대입시키는 방법

a = 123
s = 'my money is %d dollar' % a   # my money is 123 dollar

# 여러 가지 값을 넣고 싶으면 % ( , ) 사용
s = 'my number is %d, %d that' % (123 , 456)
print(s)

# 포맷 코드의 종류
"""
%d : 정수(integer)
%s : 문자열(string)
%c : 문자 1개(character)
%f : 부동소수(float-point)
%o : 8진수
%x : 16진수
"""
# 여기서 %s의 경우 정수나 부동소수같은 다른 자료형의 값을 넣어도 문자열로 변환해서 작동
# % 자체를 출력시키고 싶으면 %% 로 사용


# 포맷 코드 세부 설정
# %ns : n개 만큼의 칸을 지정하고 오른쪽부터 문자를 채움
s = '%10s Jane' % 'Hi'   # Hi 앞에 8개의 빈 칸이 생성됨
print(s)

# %-ns : 비슷하게 n개의 칸 지정하고 왼쪽부터 문자를 채움
s = '%-10s Jane' % 'Hi'


# %.nf : 소숫점 n번째 자리까지 표시
s = '원주율 : %.4f' % 3.141592 # 3.1415까지 입력
print(s)

# %k.nf 식으로 쓰면 k는 칸 확보, n은 소숫점 자리 표시



# format 함수
# %가 아닌 {n}의 형식으로 사용
s = 'I eat {0} apples'.format(3)  # I eat 3 apples

# format 안에는 변수도 가능
num = 'three'
s = 'I eat {0} apples'.format(num) # I eat three apples

# 2개 이상의 값을 넣을 때
s = 'I eat {0} {1}'.format(3, 'hamburgers') # I eat 3 hamburgers

# 0, 1 대신 전용 값 넣기
s = 'I ate {number} {name}'.format(number=3, name='pizzas') # I ate 3 pizzas


# {:n} 안에 들어갈 문자열 크기 지정
s = '{0:10} loooong'.format('hi')  # hi        loooong
print(s)

# {0:>n} - 크기 내 오른쪽 정렬
# {0:<n} - 왼쪽 정렬
# {0:^n} - 가운데 정렬

# {:n.kf} - n의 문자열 크기를 갖고 소숫점 k번째 자리수까지 표시