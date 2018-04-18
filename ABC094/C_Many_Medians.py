N = int(input())
X_list = list(map(int, input().split()))
X_list_copy = X_list.copy()
X_list_copy.sort()

median_idx = int(N / 2)
left_num = X_list_copy[median_idx - 1]
right_num = X_list_copy[median_idx]

for x in X_list:
    if x < right_num:
        print(right_num)
    else:
        print(left_num)