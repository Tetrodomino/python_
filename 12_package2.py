# __all__ : 전체 선언자 사용 시 임포드 될 모듈을 정하는 __init__ 전용 변수
# 사용은 game/sound/init 에 있음

from game.sound import * # 전체 선언자 *
echo.echo_test() # 정상 실행됨


# relative 패키지 : 다른 경로의 모듈에 선언된 모듈
# 위치는 game/graphic/render.py
from game.graphic.render import render_test2
render_test2() # echo_test가 실행


"""
relative 패키지를 사용할 때 파일의 전체 경로를 사용할 수도 있지만 상대 경로를 사용하기도 가능

. - 현재 디렉토리
.. - 부모 디렉토리
"""