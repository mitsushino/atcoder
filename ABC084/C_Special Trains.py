N = int(input())
train_list = [tuple(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    t = 0
    for j in range(i, N - 1):
        if t < train_list[j][1]:
            t = train_list[j][1]
        elif t % train_list[j][2] == 0:
            pass
        else:
            t = t + train_list[j][2] - t % train_list[j][2]
        t += train_list[j][0]
    print(t)
print(0)