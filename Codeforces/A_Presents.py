
n = int(input())
p = list(map(int, input().split()))

givers = [0] * n

for i in range(n):
    giver = i + 1
    receiver = p[i]
    givers[receiver - 1] = giver

print(*givers)