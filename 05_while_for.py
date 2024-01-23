# while
"""
while 조건문:
    실행문
"""
# 위와 같은 식으로 작성하며 조건문이 참인 동안에만 실행문을 반복
# 중간에 종료시키고 싶으면 break, 중간에 처음으로 돌아가고 싶으면 continue 사용


# for 
"""
for a in b:
    실행문
"""
# a에는 보통 b에 들어가는 변수를 의미
# b에는 리스트나 문자열, 튜플이 들어감

lists = ['a', 'b', 'c']
for a in lists: 
    print(a)    # lists에 있는 요소들이 하나씩 출력

# 이런 식으로도 사용 가능
lists = [(1, 2), (3, 4), (5, 6)]
for (a, b) in lists:
    print(a + b) # 튜플 내의 요소들이 하나씩 더해져서 출력


# 만약 다른 언어처럼 숫자를 변수에 대입하고 싶으면 range 사용
# range(a, b) : a부터 b-1 까지의 정수의 리스트가 리턴
for a in range(3):
    print(a)   # 0, 1, 2 출력