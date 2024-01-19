# 튜플
# 리스트랑 비슷하지만 내부 항목의 값이 수정 불가능한 자료형

# ( ) 안에 변수를 묶어서 생성
a = (1, 2, 3)
a =  1, 2, 3   # 그냥 괄호 없이 만들어도 튜플로 취급

# 튜플은 내부 항목의 값을 삭제하는 것도 불가능
del a[0] # 오류 발생

# 인덱싱이나 슬라이싱은 리스트와 동일
# 곱하기, 튜플끼리 더하기는 가능하지만 새 튜플에 대입하는 방식으로만 생성 가능
# 튜플 자체의 값 변경이 있을 수 있는 insert나 pop 등의 함수는 없음