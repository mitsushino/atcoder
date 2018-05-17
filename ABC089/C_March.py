from itertools import combinations

N = int(input())
d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for _ in range(N):
    fl = input()[0]
    if fl in d:
        d[fl] += 1

s_comb_list = list(combinations('MARCH', 3))
v = 0
for s_comb in s_comb_list:
    v += (d[s_comb[0]] * d[s_comb[1]] * d[s_comb[2]])
print(v)