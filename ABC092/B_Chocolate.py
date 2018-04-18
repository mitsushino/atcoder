N = int(input())
D, X = map(int, input().split())
chocolates = [X]
for i in range(N):
    A = int(input())
    chocolates.append(1)
    for j in range(1, 101):
        if j * A + 1 > D:
            break
        else:
            chocolates.append(1)
print(sum(chocolates))