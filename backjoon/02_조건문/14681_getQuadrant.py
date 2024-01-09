# 특정 지점의 사분면 구하기
# 2 │ 1
# ──┼──
# 3 │ 4

x = int(input())
y = int(input())
q = 0

if x > 0:
    q = 1 if y > 0 else 4
else:
    q = 2 if y > 0 else 3

print(q)