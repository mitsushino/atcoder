# https://beta.atcoder.jp/contests/abc098/tasks/arc098_b
# しゃくとり法

N = int(input())
A_list = list(map(int, input().split()))

num_sum = 0
xor_sum = 0
idx = 0
r = 0
count = 0
for l in range(0, N):
    while r < N and num_sum + A_list[r] == xor_sum ^ A_list[r]:
        num_sum += A_list[r]
        xor_sum ^= A_list[r]
        r += 1
    num_sum -= A_list[l]
    xor_sum ^= A_list[l]
    count += (r - l)
print(count)