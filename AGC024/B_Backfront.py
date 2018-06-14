N = int(input())
n_list_idx = [0 for _ in range(N + 1)]
for i in range(N):
    v = int(input())
    n_list_idx[v] = i

o_max = 1
o = 1
for i in range(2, len(n_list_idx)):
    if n_list_idx[i] > n_list_idx[i - 1]:
        o += 1
    else:
        if o > o_max:
            o_max = o
        o = 1
if o > o_max:
    o_max = o
print(N - o_max)