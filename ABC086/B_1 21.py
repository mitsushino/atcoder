import math

a, b = map(int, input().split())
ab = int('{}{}'.format(a, b))
if ab == math.floor(math.sqrt(ab)) ** 2:
    print('Yes')
else:
    print('No')