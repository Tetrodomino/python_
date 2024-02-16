def render_test():
    print("render")


# relative 패키지
# 다른 디렉토리의 모듈을 호출하기
from game.sound.echo import echo_test

def render_test2():
    echo_test()