n, m = map(int, input().split())
tasks = [int(x) for x in input().split()]

distances = tasks[0] - 1

for i in range(1, m):
    if tasks[i] < tasks[i-1]:
        distances += (n - tasks[i-1] + tasks[i])

    else:
        distances += tasks[i] - tasks[i-1]

print(distances)