N = int(input())
S_list = [input() for _ in range(N)]
cnt = 0


def count_symmetry(S_symmetry):
    for i in range(N):
        for j in range(i + 1, N):
            if S_symmetry[i][j] != S_symmetry[j][i]:
                return False
    return True


for k in range(N):
    S_symmetry = S_list[k:] + S_list[:k]
    if count_symmetry(S_symmetry):
        cnt += 1

print(cnt * N)