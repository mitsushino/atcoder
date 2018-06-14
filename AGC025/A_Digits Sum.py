N = int(input())

min_num = float('inf')
for i in range(1, N):
    j = N - i
    A_sum = sum(map(int, list(str(i))))
    B_sum = sum(map(int, list(str(j))))
    if A_sum + B_sum < min_num:
        min_num = A_sum + B_sum
print(min_num)