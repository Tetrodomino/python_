# 클래스
# 다양한 객체를 만들어내기 위한 틀

class Class1: # 빈 클래스
    pass

# 클래스 선언하기 (a는 Class1의 인스턴스)
a = Class1()
print(type(a)) # '__main__.Class1'


# 사칙연산 클래스 만들기
class FourCal:

    # 생성자
    # 클래스를 생성할 때 매개변수를 넣어 사용할 수 있음
    # __ __ 사이에 init을 넣어서 만들기 가능
    def __init__(self, first, second):
        self.first = first
        self.second = second # 해당 생성자를 만들면 더 이상 빈 생성자는 사용되지 않음

    # 변수를 대입하는 메서드
    def setdata(self, first, second): 
        self.first = first # 객체에 first라는 변수가 생성되고 first 매개변수가 전달됨
        self.second = second

    """
    메서드에 사용되는 첫 번째 매개변수(위에는 self)는 인스턴스 자신이 전달됨
    가령 setdata를 위와 같이 하고 a.setdata(4, 2) 식으로 호출하면
    a의 첫 번째 변수는 4, a의 2번째 변수는 2가 대입되는 방식

    첫 번째 매개변수의 이름은 대체로 self를 쓰나 다른 이름을 사용하더라도 무방하고
    모든 메서드에는 반드시 self에 대응하는 매개변수가 필요
    """

    # 두 변수를 더하는 메서드
    def add(self):
        result = self.first + self.second
        return result
    
    # 곱하기
    def mul(self):
        result = self.first * self.second
        return result
    
    # 빼기
    def sub(self):
        result = self.first - self.second
        return result
    
    # 나누기
    def div(self):
        result = self.first / self.second
        return result
    
    def add2(self, a, b):
        return a + b

a = FourCal(1, 2)
a.setdata(5, 10)
print(a.first) # 5

print(a.mul()) # 50 

print(a.add2(2, 4)) # 6

a = FourCal(1, 2)
print(a.add())


# 클래스의 상속
# 다른 클래스의 기능을 같이 사용 가능
class MoreFourCal(FourCal): # 괄호 안에 다른 클래스를 넣어서 생성 가능
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(6, 3)
print(a.div()) # 2.0

print(a.pow())


# 오버라이딩
# 상속받은 클래스의 메서드를 재정의
# 오버라이드를 하면 해당 메서드를 사용할 때 오버라이드 된 메서드가 실행됨
class SafeFourCal(FourCal):
    def div(self): # 0으로 나누면 오류가 아닌 0이 출력되도록 div 재정의
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
a = SafeFourCal(4, 0)
print(a.div()) # 0


# 클래스 변수
# 클래스 내부에 별도로 선언된 변수
class nums:
    a = 1

a = nums()
print(a.a) # 1

# 클래스 변수를 '클래스명.클래스변수명' 을 사용해서 직접 수정할 경우 다른 객체에도 일괄 적용됨
b = nums()
nums.a = 2 # nums 전체의 a를 2로 변경
print(b.a, a.a) # 2 2

# 만일 객체의 클래스 변수를 그냥 수정하면 해당 변수는 클래스 변수가 아닌 새로 생성된 객체변수로 취급
a.a = 3 # 클래스변수가 아닌 .first 같은 객체변수로 취급
print(a.a) # 3
