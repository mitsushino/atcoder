N = int(input())
candies = []
for _ in range(2):
    candies.append(list(map(int, input().split())))

max_candies_num = 0
for i in range(N):
    first_row_candies = sum(candies[0][:i + 1])
    second_row_candies = sum(candies[1][i:])
    sum_candies = first_row_candies + second_row_candies
    if sum_candies > max_candies_num:
        max_candies_num = sum_candies
print(max_candies_num)