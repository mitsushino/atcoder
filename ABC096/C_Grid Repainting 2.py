import sys

H, W = map(int, input().split())
s_list = [list(input()) for _ in range(H)]


def judge_black(y, x):
    if 0 <= y - 1 < H:
        if s_list[y - 1][x] == '#':
            return True
    if 0 <= x - 1 < W:
        if s_list[y][x - 1] == '#':
            return True
    if 0 <= x + 1 < W:
        if s_list[y][x + 1] == '#':
            return True
    if 0 <= y + 1 < H:
        if s_list[y + 1][x] == '#':
            return True
    return False


for i in range(H):
    for j in range(W):
        if s_list[i][j] == '#':
            if judge_black(i, j) is False:
                print('No')
                sys.exit()
print('Yes')