n = int(input())

goals = []

for i in range(n):
    goals.append(input())

unique = list(set(goals))

points1 = goals.count(unique[0])
points2 = 0

if len(unique) == 2:
    points2 = goals.count(unique[1])

if points1 > points2:
    print(unique[0])

else:
    print(unique[1])