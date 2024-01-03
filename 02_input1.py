# 입력함수 input
# 변수 = input('출력할 텍스트') 식으로 작성

num1 = input() #비우는 것도 가능

print(num1)

num2 = input("숫자를 입력하십시오: ")

print(num2)

str = input("텍스트 입력: ")

print(str)

print(num1 + num2) # input의 값은 문자열로 취급돼서
                   # 이렇게 하면 두 숫자의 합이 아닌 두 숫자가 붙어서 출력됨
                   # ex) 5, 6 입력 → 56 출력 
