import sys

N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N - i + 1):
        k = N - (i + j)
        if (i * 10000) + (j * 5000) + (k * 1000) == Y:
            print('{} {} {}'.format(i, j, k))
            sys.exit()
print('-1 -1 -1')