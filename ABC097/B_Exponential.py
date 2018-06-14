X = int(input())

exponential = {1}
for i in range(2, 32):
    for j in range(2, 11):
        if i ** j <= X:
            exponential.add(i ** j)
        else:
            break
print(max(exponential))