# 딕셔너리
# Key를 통해 Value를 저장하는 자료형

# {'key': value} 형태로 선언
a = {'name': 'apple', 'number': 50, 'price': [1000, 1500, 2000]}

# a[i] = k : i의 키를 가진 k값 추가
a['location'] = '한국'
print(a) # {'name': 'apple', 'number': 50, 'price': [1000, 1500, 2000], 'location': '한국'}

# del a[i] : i의 키를 가진 데이터 삭제
del a['location']
print(a) # {'name': 'apple', 'number': 50, 'price': [1000, 1500, 2000]}

# 딕셔너리는 슬라이싱 없이 인덱싱만으로 값 출력
print(a['price'])


# keys() : key 값만 모아 리턴. 형태는 dict_keys([])
print(a.keys()) # dict_keys(['name', 'number', 'price'])

# dict_keys는 for에서 사용할 수 있지만 리스트 특유의 append나 sort 등은 불가능


# values() : 비슷하게 value 값만 모아서 dict_values([]) 형태로 리턴
print(a.values()) # dict_values(['apple', 50, [1000, 1500, 2000]])


# items() : (key, value) 같은 튜플 형태로 리턴
print(a.items()) # dict_items([('name', 'apple'), ('number', 50), ('price', [1000, 1500, 2000])])


# clear() : 딕셔너리 안의 모든 항목 삭제
print(a.clear()) # None


# get(key) : key 값에 해당하는 value 리턴. 인덱싱과의 차이점은 없는 key 값을 넣으면 오류가 아니라 None 반환
a = {'name': 'apple', 'number': 50, 'price': [1000, 1500, 2000]}
print(a.get('name')) # apple


# key in a : a 딕셔너리 안에 key가 있는지 확인
print('age' in a) # False;