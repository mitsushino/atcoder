N, K = map(int, input().split())

if N == 1:
    print(K)
else:
    p = K
    for _ in range(N - 1):
        p *= (K - 1)
    print(p)