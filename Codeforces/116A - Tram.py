n = int(input())
intrain = 0
maxintrain = []
for i in range(n):
    a, b = map(int, input().split())
    intrain = intrain + b - a
    maxintrain.append(intrain)

print(max(maxintrain))