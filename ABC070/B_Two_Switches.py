A, B, C, D = map(int, input().split())
d_AB = B - A
d_DC = D - C
set_AB = set()
set_CD = set()
for i in range(A, B + 1):
    set_AB.add(i)
for i in range(C, D + 1):
    set_CD.add(i)
if len(set_AB.intersection(set_CD)) == 0:
    print(0)
else:
    print(len(set_AB.intersection(set_CD)) - 1)