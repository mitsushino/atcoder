s = input()
K = int(input())

s_set = set()
for i in range(len(s)):
    for j in range(i + 1, i + K + 1):
        if j > len(s) + 1:
            break
        s_set.add(s[i:j])
s_list = list(s_set)
s_list.sort()
print(s_list[K - 1])