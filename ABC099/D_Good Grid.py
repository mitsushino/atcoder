N, C = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(int, input().split())) for _ in range(N)]

group = [[] for _ in range(3)]

for i in range(N):
    for j in range(N):
        group[(i + j) % 3].append(grid[i][j])

color_costs = [[] for _ in range(C)]
for i in range(3):
    cost = 0
    for j in range(1, C + 1):
        for k in group[i]:
            cost += costs[k - 1][j - 1]
        color_costs[i].append(cost)
        cost = 0

min_cost = float('inf')
ccost = 0
offset = 0
for i in range(len(color_costs)):
    ccost = 0
    for j in range(len(color_costs)):
        ccost += color_costs[j][(j + offset) % C]
    offset += 1
    if min_cost > ccost:
        min_cost = ccost
print(min_cost)