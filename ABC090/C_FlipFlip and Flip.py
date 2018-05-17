N, M = map(int, input().split())
N -= 2
M -= 2
if N < 0:
    N = 1
if M < 0:
    M = 1
print(N * M)