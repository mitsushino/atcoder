X, Y = map(int, input().split())
cnt = 1
X *= 2
while X <= Y:
    X *= 2
    cnt += 1
print(cnt)