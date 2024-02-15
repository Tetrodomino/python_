# 모듈 파일 1
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 만약 모듈 파일을 직접 실행시키고자 할 때는 __name__ 라는 특수 변수 사용
# 직접 실행할 때는 __name__ 변수에 "__main__" 값이 저장되어 실행되지만
# 다른 파일에서 임포트했을 때는 __name__에 모듈 이름(mod1)이 저장되기 때문에 실행되지 않음
# 이 과정을 거치지 않으면 임포트만 해도 아래 문구가 실행되는 문제 발생
if __name__ == "__main__":
    print(add(1, 3))
    print(sub(4, 2))