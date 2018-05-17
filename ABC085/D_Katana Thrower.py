import sys
import math

N, H = map(int, input().split())
katana_list = [tuple(map(int, input().split())) for _ in range(N)]
katana_list.sort(reverse=True)
cut_max = katana_list[0][0]

katana_list = [tuple([katana[0], katana[1]]) for katana in katana_list \
               if katana[1] >= cut_max]
katana_list.sort(key=lambda x: x[1], reverse=True)

cnt = 0
for katana in katana_list:
    H -= katana[1]
    cnt += 1
    if H <= 0:
        print(cnt)
        sys.exit()

katana_list.sort(reverse=True)
cnt += math.ceil(H / katana_list[0][0])
print(cnt)