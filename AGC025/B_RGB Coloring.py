import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N, A, B, K = map(int, input().split())

sum_p = 0
for a in range(N + 1):
    b = (K - (a * A)) / B
    if int(b) == b:
        sum_p += (combinations_count(N, a) * combinations_count(N, b)) % 998244353
print(sum_p % 998244353)