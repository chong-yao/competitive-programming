n = int(input())
x = [int(x) for x in input().split()[1:]]
y = [int(y) for y in input().split()[1:]]

xy = set(x + y)

levels = set(range(1, n+1))

if levels==xy:
    print("I become the guy.")

else:
    print("Oh, my keyboard!")