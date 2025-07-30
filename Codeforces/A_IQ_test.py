n = int(input())
nums = [int(x) for x in input().split()]

evens = []
odds = []

for i in nums:
    if i%2 == 0:
        evens.append(i)

    else:
        odds.append(i)

if len(evens) == 1:
    print(nums.index(evens[0]) + 1)

else:
    print(nums.index(odds[0]) + 1)