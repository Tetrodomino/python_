# 리스트의 함수

# append() : 맨 마지막에 새 항목 추가, 추가되는 자료형에는 제한 없음
a = [1, 2, 3]
a.append(4)
print(a) # [1, 2, 3, 4]


# sort() : 리스트 정렬
a = [3, 1, 2]
a.sort()
print(a) # [1, 2, 3]

# 알파벳도 정렬 가능
a = ['a', 'c', 'b']
a.sort()
print(a) # ['a', 'b', 'c']


# reverse() : 리스트를 반대 순서로 뒤집기
a.reverse()
print(a) # ['c', 'b', 'a']


# index(n) : n이 리스트에 있을 경우 그 위치 반환. 없으면 오류 발생
a = [1, 2, 3, 4, 5]
print(a.index(2)) # 1


# insert(a, b) : 리스트의 a번째 위치에 b 삽입
a.insert(0, 0)
print(a) # [0, 1, 2, 3, 4, 5]


# remove(n) : 왼쪽에서부터 세어 첫 번째로 나오는 n 삭제
a.remove(4)
print(a) # [0, 1, 2, 3, 5]


# pop() : 리스트의 맨 마지막 요소를 반환하고 해당 요소는 원 리스트에서 삭제
print(a.pop()) # 5
print(a) # [0, 1, 2, 3]

# pop(n) : 리스트의 n번째 요소를 반환하고 해당 요소는 원 리스트에서 삭제


# count(n) : 리스트 안에 n이 몇 개 있는지 반환
a = [1, 1, 2, 1, 0, 1]
print(a.count(1)) # 4


# extend([]) : 리스트를 뒤에 붙여서 확장. 리스트끼리 더하기랑 기능 같음
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a) # [1, 2, 3, 4, 5]