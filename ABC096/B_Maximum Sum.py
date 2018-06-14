abc_list = list(map(int, input().split()))
K = int(input())
abc_list.sort()
m_v = abc_list.pop()

for i in range(K):
    m_v *= 2
abc_list.append(m_v)
print(sum(abc_list))