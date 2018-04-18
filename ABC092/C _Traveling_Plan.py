N = int(input())
A_list = [0]
A_list.extend(list(map(int, input().split())))
A_list.append(0)
previous_val = 0
S = 0
for i in A_list[1:]:
    S += abs(previous_val - i)
    previous_val = i

for idx, val in enumerate(A_list):
    if idx == 0 or idx == (len(A_list) - 1):
        continue
    else:
        new_dif = abs(A_list[idx - 1] - A_list[idx + 1])
        old_dif = abs(A_list[idx - 1] - A_list[idx]) + abs(A_list[idx] - A_list[idx + 1])
        print(S + new_dif - old_dif)