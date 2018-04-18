import sys

n = int(input())
prev_t = 0
prev_x = 0
prev_y = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    d_t = abs(prev_t - t)
    d_x = abs(prev_x - x)
    d_y = abs(prev_y - y)
    if d_t % 2 != ((d_x + d_y) % 2) or d_t < d_x + d_y:
        print('No')
        sys.exit()
    prev_t = t
    prev_x = x
    prev_y = y
print('Yes')