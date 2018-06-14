from collections import Counter

N = int(input())
a = list(map(int, input().split()))
c = Counter(a)

cnt = 0
for k, v in c.items():
    if v == 0:
        continue
    if k > v:
        cnt += v
    elif k < v:
        cnt += (v - k)
print(cnt)