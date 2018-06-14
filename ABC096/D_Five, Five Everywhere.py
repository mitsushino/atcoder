n = int(input())


def create_prime_table(n):
    list = [True for _ in range(n + 1)]
    i = 2
    while i * i <= n:
        if list[i]:
            j = i + i
            while j <= n:
                list[j] = False
                j += i
        i += 1

    table = [i for i in range(n + 1) if list[i] and i >= 2]
    return table


prime = create_prime_table(55555)
cnt = 0
nine = []
for idx, i in enumerate(prime):
    if (i % 100) == 9:
        nine.append(i)
print(*nine[:n])