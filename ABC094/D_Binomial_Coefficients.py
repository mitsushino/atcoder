n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
max_num = max(a_list)
a_list.pop()
n_half = max_num / 2
a_list_dif = [abs(i - n_half) for i in a_list]
min_idx = 0
min_val = 10 ** 10
for idx, v in enumerate(a_list_dif):
    if v < min_val:
        min_idx = idx
        min_val = v
print(max_num, a_list[min_idx])