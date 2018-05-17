N, A, B = map(int, input().split())
N_list = [str(i) for i in range(1, N + 1)]
total = 0
for i in N_list:
    subtotal = 0
    for s in i:
        subtotal += int(s)
    if A <= subtotal <= B:
        total += int(i)
print(total)