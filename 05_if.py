# IF
"""
if 조건문:
    실행문
"""
# 위와 같은 형태로 작성
# 실행문의 들여쓰기는 항상 한 if 내에서는 일정해야 함

if True:
    print("항상 실행")


# 비교연산자 및 각종 비교문
"""
1. == : 같음
2. != : 같지 않음
3. >  : 큼
4. <  : 작음
5. >= : 크거나 같음
6. <= : 작거나 같음

a and b : a, b 조건 모두 만족해야 참
a or b : a, b 조건 중 하나 만족해야 참
not a : a를 만족하지 않으면 참

a in [] : 리스트 내에 a가 있으면 참, 리스트 대신 튜플이나 문자열도 사용 가능
a not in [] : 리스트 내에 a가 없으면 참
"""


# elif
"""
if 조건문:
    실행문
elif 조건문2:
    실행문2
"""
# 위와 같은 식으로 작성


# 조건부 표현식 (삼항연산자 대용)
# python에서는 삼항연산자 '?' 가 없어서 이 방식으로 사용
"""
a if 조건문 else b
조건문이 참일 경우 a, 거짓일 경우 b가 실행
"""