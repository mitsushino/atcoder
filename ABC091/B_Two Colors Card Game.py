from collections import Counter

N = int(input())
blue_list = [input() for _ in range(N)]
blue = Counter(blue_list)

M = int(input())
red_list = [input() for _ in range(M)]
red = Counter(red_list)

blue.subtract(red)
c = blue.most_common(1)[0][1]
if c < 0:
    print(0)
else:
    print(c)