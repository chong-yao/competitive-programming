n = float(input())
p = list(int(x) for x in input().split())
vol = 0
for i in range(int(n)):
    vol += (p[i] / 100)

print(100*vol / n)