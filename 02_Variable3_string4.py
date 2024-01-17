# (5) 문자열 관련 함수

s = 'aabbb ca bb aaaa b'

# count - 문자열 내 특정 문자의 개수 세기
print(s.count('b')) # 6

# find - 왼쪽에서부터 세어 특정 문자의 위치 찾기 (없을 경우 -1)
print(s.find('b')) # 2

# index - find랑 똑같이 찾지만 없을 경우 오류 발생
print(s.index('c')) # 6

# join - 문자열 사이에 문자열 삽입하기
insert = 'bb'
s2 = 'aaa'
print(insert.join(s2)) # abbabba

# upper() - 소문자를 대문자로
# lower() - 대문자를 소문자로

# strip() - 문자열 양쪽 끝의 공백 모두 지우기, 왼쪽만이면 lstrip, 오른쪽만이면 rstrip
s = ' a b c d '
print(s.strip()) # 'a b c d'

# replace(s1, s2) - 문자열 내의 모든 s1 문자열을 s2로 변환
s = 'aa a aa baa bcaab'
print(s.replace('aa', 'x')) # x a x bx bcxb

# split(s) - 문자열을 s 문자열을 기준으로 분할. 만약 s를 넣지 않으면 공백을 기준으로 분할
print(s.split()) # ['aa', 'a', 'aa', 'baa', 'bcaab']