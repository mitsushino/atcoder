N, C = map(int, input().split())
sushi_list = []
for _ in range(N):
    sushi_list.append(tuple(map(int, input().split())))

clock = [0]
clock_double = [0]

cal = 0
for idx, sushi in enumerate(sushi_list, 1):
    cal += sushi[1]
    clock.append(max(clock[idx - 1], cal - sushi[0]))
    clock_double.append(max(clock_double[idx - 1], cal - sushi[0] * 2))

cal = 0
rev_clock = [0]
rev_clock_double = [0]
for idx, sushi in enumerate(sushi_list[::-1], 1):
    cal += sushi[1]
    rev_clock.append(max(rev_clock[idx - 1], cal - (C - sushi[0])))
    rev_clock_double.append(max(rev_clock_double[idx - 1], cal - (C - sushi[0]) * 2))

max_cal = 0
for i in range(N + 1):
    c = clock_double[i] + rev_clock[N - i]
    r_c = rev_clock_double[i] + clock[N - i]
    max_cal = max(max_cal, c, r_c)
print(max_cal)