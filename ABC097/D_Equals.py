# UnionFindで参考にしたページ
# http://www.geocities.jp/m_hiroi/light/pyalgo61.html


# 集合の代表を求める
def find(x):
    if link[x] < 0:
        return x
    else:
        # 経路の圧縮
        link[x] = find(link[x])
        return link[x]


# 併合
def union(x, y):
    s1 = find(x)
    s2 = find(y)
    if s1 != s2:
        if link[s1] >= link[s2]:
            # 小さいほうが個数が多い
            link[s2] += link[s1]
            link[s1] = s2
        else:
            link[s1] += link[s2]
            link[s2] = s1
        return True
    return False


N, M = map(int, input().split())
p = list(map(int, input().split()))
link = [-1 for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)

cnt = 0
for i in range(1, N + 1):
    if find(i) == find(p[i - 1]):
        cnt += 1
print(cnt)