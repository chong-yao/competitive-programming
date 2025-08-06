from collections import Counter
from math import ceil

n = int(input())
groups = [int(x) for x in input.split()]

count = Counter(groups)
taxis = 0

# Groups of 4 each get a taxi
taxis += count[4]

# Pair group of 3 with group of 1
pair = min(count[3], count[1])
taxis += pair
count[3] -= pair
count[1] -= pair

# Remaining 3s need own taxi
taxis += count[3]

# Pair groups of 2 together
taxis += count[2] // 2
if count[2] % 2:
    taxis += 1
    count[1] -= min(2, count[1])

# Remaining 1s, 4 per taxi
if count[1] > 0:
    taxis += ceil(count[1] / 4)

print(taxis)
