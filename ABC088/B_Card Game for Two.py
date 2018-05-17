N = int(input())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)
Alice = []
Bob = []
for idx, v in enumerate(a_list):
    if idx % 2 == 0:
        Alice.append(v)
    else:
        Bob.append(v)
print(sum(Alice) - sum(Bob))