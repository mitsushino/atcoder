N, X = map(int, input().split())
donuts = []
for _ in range(N):
    donuts.append(int(input()))

cnt = len(donuts)
for d in donuts:
    X -= d
min_d = min(donuts)
while X >= min_d:
    X -= min_d
    cnt += 1
print(cnt)