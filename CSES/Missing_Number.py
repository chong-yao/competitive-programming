n = int(input())

numbers = [int(x) for x in input().split()]

for i in range(1, n+1):
    if i not in numbers:
        print(i)