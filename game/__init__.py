# __init__ 파일은 해당 폴더가 패키지의 일부임을 알려주는 역할을 함

"""
python 3.3 부터 __init__ 의 사용이 의무는 아니나
쓰는 것이 권장
"""

# 보통 패키지와 관련된 설정이나 초기화 코드를 넣는 경우가 많음

version = 3.5

def print_version_info():
    print("The version of this game is %.1f" % (version))


# init 파일에 다른 모듈을 임포트하여 사용 가능
from .graphic.render import render_test # 이제 game을 임포트하면 render_test() 메서드도 사용 가능


# 패키지를 임포트할 때 실행되는 문구 설정
print("initializing game package") # 12_package를 실행하면 가장 먼저 실행됨
