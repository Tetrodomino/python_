# 프로그램의 입출력

import sys      # 프로그램에 인수를 전달하는 모듈



"""
CMD창에서 09_IO.py를 실행하면 띄어쓰기로 입력을 구분하여 실행됨

여기서 argv[0] 은 09_IO.py(파일명)이 되고 argv[1]부터 하나씩 args에 대입됨
""" 
args = sys.argv[1:]
for i in args:
    print(i)

