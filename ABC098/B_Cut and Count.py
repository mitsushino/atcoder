N = int(input())
S = input()

max_s = 0
for i in range(1, N):
    X = set(S[:i])
    Y = set(S[i:])
    if len(X & Y) > max_s:
        max_s = len(X & Y)
print(max_s)