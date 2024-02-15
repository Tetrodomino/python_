# 패키지
# 모듈의 집합

"""
패키지 사용법 2가지
"""
# game 패키지의 sound 폴더의 echo 파일을 모듈로 임포트
import game.sound.echo as gg
gg.echo_test()

# from을 통해 경로를 지정하고 echo 파일을 임포트
from game.sound import echo
echo.echo_test()

""" 주의사항 """
# game만 임포트하면 game에 바로 있는 __init__에 정의된 것만 사용 가능
import game
"""
game.sound.echo.echo_test() - ModuleNotFoundError 오류 발생
"""


# __init__.py 파일 사용
# init 파일의 설명은 game/__init__.py 참조
print(game.version) # 3.5
game.print_version_info()
game.render_test()