# 파일
# open 함수를 통해 파일에 접근 가능
f = open("새파일.txt", 'w') # 실행하면 실제로 새파일.txt가 생성됨
f.close() # 다른 파일에 접근하려면 close로 접근 해제해야 함

"""
open의 2번째 매개변수의 의미
w : 파일에 내용을 쓸 때 사용, 파일이 없으면 생성
r : 파일의 내용을 읽을 때 사용
a : 파일의 마지막에 내용을 추가할 때 사용
"""

# 특정 위치에 파일 생성
# 폴더 구분자는 / 말고 \\로도 가능
f = open("C:/python/backjoon/새파일.txt", 'w')

# 열어둔 파일에 내용 추가
for i in range(1, 11):
    f.write("%d번째 줄입니다.\n" % i)

f.close()


################## 파일 내용 읽기 ###################
# readline 사용
f = open("C:/python/backjoon/새파일.txt", 'r') # r로 선언
line = f.readline() # 1번째 줄 읽음
print(line)

# readlines : 모든 줄 읽기
while True:
    line = f.readline()
    line = line.strip() # 끝에 있는 \n 제거
    if not line: break
    print(line)

f.close() # 이거 안 하면 파일 읽던 내용이 초기화되지 않음

# readlines는 파일의 각 행을 리스트로 만듦
f = open("C:/python/backjoon/새파일.txt", 'r')
lines = f.readlines()
print(lines)

f.close()

# read 함수 사용
f = open("C:/python/backjoon/새파일.txt", 'r')
data = f.read() # 파일 내용 전체 읽기
print(data)

f.close()

# 객체에서 바로 for 사용
f = open("C:/python/backjoon/새파일.txt", 'r')
for line in f:
    print(line)
f.close()


################### 파일에 새로운 내용 추가 ##################
f = open("C:/python/backjoon/새파일2.txt", 'w') # 다른 파일 생성
f.close()

# write를 통해 내용 추가
f = open("C:/python/backjoon/새파일2.txt", 'a') # 덮어쓰기가 아닌 추가를 할 땐 a를 사용
for i in range(1 , 11):
    f.write("%d번째 줄\n" % i)
    
f.close()
f = open("C:/python/backjoon/새파일2.txt", 'a') 
for i in range(1 , 11):
    f.write("%d번째 줄\n" % i)

f.close()