N = int(input())
A_list = [0]
for i in range(N):
    A_list.append(int(input()))
A_flag = [False] * len(A_list)

idx = 1
count = 1
while True:
    if A_list[idx] == 2:
        print(count)
        break
    if A_flag[idx] is True:
        print(-1)
        break
    A_flag[idx] = True
    idx = A_list[idx]
    count += 1