# 문자열 포매팅
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


# 

