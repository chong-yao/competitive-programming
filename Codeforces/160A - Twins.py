n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
total_sum = sum(coins)
running_sum = 0
i=0

for coin in coins:
    running_sum += coin
    i+=1
    if running_sum > total_sum - running_sum:
        break

print(i)