def find_mine_num(H, W, S, current_H, current_W):
    if S[current_H][current_W] == '#':
        return '#'
    mine_count = 0
    # 左斜め上、上、右斜め上
    find_H_position = current_H - 1
    for i in range(-1, 2):
        find_W_position = current_W + i
        if 0 <= find_H_position < H and 0 <= find_W_position < W:
            if S[find_H_position][find_W_position] == '#':
                mine_count += 1
    # 左、右
    if 0 <= current_W - 1 < W:
        if S[current_H][current_W - 1] == '#':
            mine_count += 1
    if 0 <= current_W + 1 < W:
        if S[current_H][current_W + 1] == '#':
            mine_count += 1
    # 左斜め下、下、右斜め下
    find_H_position = current_H + 1
    for i in range(-1, 2):
        find_W_position = current_W + i
        if 0 <= find_H_position < H and 0 <= find_W_position < W:
            if S[find_H_position][find_W_position] == '#':
                mine_count += 1
    return mine_count


H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))
S_mine = []
for i in range(H):
    mine = []
    for j in range(W):
        mine.append(find_mine_num(H, W, S, i, j))
    S_mine.append(mine)
for s in S_mine:
    print(*s, sep='')