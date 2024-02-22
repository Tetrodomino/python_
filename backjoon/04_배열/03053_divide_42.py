# 42로 나눈 나머지의 개수 구하기

nums = []
for i in range(10):
    a = int(input()) % 42
    if len(nums) == 0 or nums.count(a) == 0:
        nums.append(a)
    
print(len(nums))