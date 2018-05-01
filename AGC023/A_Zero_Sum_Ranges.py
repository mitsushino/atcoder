from itertools import accumulate
from collections import Counter

N = int(input())
num_list = list(map(int, input().split()))
cumulative_sum_list = list(accumulate(num_list))
cumulative_sum_list.append(0)

c = Counter(cumulative_sum_list)
s = 0
for i in c.values():
    s += i * (i - 1) // 2
print(s)