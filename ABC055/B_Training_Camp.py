N = int(input())
m = 10 ** 9 + 7
power = 1
for i in range(1, N + 1):
    power *= i
    power %= m
print(power)