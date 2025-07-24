n, h = map(int, input().split())
a = list(int(x) for x in input().split())
bent = 0
for j in range(len(a)):
    if a[j] > h:
        bent += 1

print(bent * 2 + n - bent)