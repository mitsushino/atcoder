N, M, X = map(int, input().split())
A_list = map(int, input().split())

road_list = [0] * (N + 1)
for i in A_list:
    road_list[i] = 1

right = sum(road_list[X:])
left = sum(road_list[:X])
print(min(right, left))