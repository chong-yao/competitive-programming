n, l = map(int, input().split())

lanterns = sorted([int(x) for x in input().split()])

max_dist = 0

for i in range(len(lanterns)-1):
    current_dist = lanterns[i+1] - lanterns[i]

    if current_dist > max_dist:
        max_dist = current_dist

print(max_dist)