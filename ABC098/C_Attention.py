from collections import Counter

N = int(input())
S = input()
c = Counter(S[1:])
E_count = c['E']
min_count = E_count

W_left = 0
E_right = E_count
for i in range(1, N):
    if S[i - 1] == 'W':
        W_left += 1
    if S[i] == 'E':
        E_right -= 1
    if W_left + E_right < min_count:
        min_count = W_left + E_right
print(min_count)