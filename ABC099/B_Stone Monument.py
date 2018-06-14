towers = [0]
for i in range(1, 1000):
    towers.append(towers[i - 1] + i)
a, b = map(int, input().split())

B = b - a

print(towers[B] - b)