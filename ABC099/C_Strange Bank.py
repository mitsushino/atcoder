N = int(input())
l = [1, 6, 9, 36, 81, 216, 729, 1296, 6561, 7776, 46656, 59049]
dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(12):
    for j in range(l[i], N + 1):
        dp[j] = min(dp[j], dp[j - l[i]] + 1)
print(dp[N])