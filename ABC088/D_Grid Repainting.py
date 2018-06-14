from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
dot_cnt = 0
for g in grid:
    dot_cnt += g.count('.')
sy = 0
sx = 0
gy = H - 1
gx = W - 1

deq = deque()
deq.append((0, 0))
grid[0][0] = 0

y_list = [-1, 1, 0, 0]
x_list = [0, 0, -1, 1]

while deq:
    y, x = deq.popleft()
    if y == gy and x == gx:
        break
    for i in range(len(y_list)):
        dy = y + y_list[i]
        dx = x + x_list[i]
        if dy < 0 or H <= dy or dx < 0 or W <= dx:
            continue
        if grid[dy][dx] == '.':
            deq.append((dy, dx))
            grid[dy][dx] = grid[y][x] + 1
if grid[gy][gx] == '.':
    print(-1)
else:
    print(dot_cnt - (grid[gy][gx] + 1))
from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
dot_cnt = 0
for g in grid:
    dot_cnt += g.count('.')
sy = 0
sx = 0
gy = H - 1
gx = W - 1

deq = deque()
deq.append((0, 0))
grid[0][0] = 0

y_list = [-1, 1, 0, 0]
x_list = [0, 0, -1, 1]

while deq:
    y, x = deq.popleft()
    if y == gy and x == gx:
        break
    for i in range(len(y_list)):
        dy = y + y_list[i]
        dx = x + x_list[i]
        if dy < 0 or H <= dy or dx < 0 or W <= dx:
            continue
        if grid[dy][dx] == '.':
            deq.append((dy, dx))
            grid[dy][dx] = grid[y][x] + 1
if grid[gy][gx] == '.':
    print(-1)
else:
    print(dot_cnt - (grid[gy][gx] + 1))
