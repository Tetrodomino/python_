# 모듈
# 다른 파이썬 파일에서 함수나 클래스 등을 사용할 때 참조하는 것

import random # random 모듈에 접근

# 모듈의 경로를 알아내려면 inspect 모듈의 getfile() 함수 사용
import inspect
print(inspect.getfile(random)) # random 모듈의 경로


# 파이썬 파일을 모듈로 사용하고 싶으면 sys 모듈을 사용
import sys
"""
모듈을 추가하려면 sys.path.append 사용
append 괄호 안에는 해당 모듈의 경로를 적어넣으면 됨

sys.path.append("C:/python/mod1.py") 
"""
#print(sys.path) # 설치된 모듈 확인

# 새로 설치한 모듈 사용해보기
import mod1 
print(mod1.add(2, 4))

# 모듈 2 사용
import mod2
print(mod2.pi)
print(mod2.Math().circle(3))

# 같은 폴더에 있는 파일은 별도 추가 과정 없이도 사용 가능
import mod3
print(mod3.mul(3, 6))