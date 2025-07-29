n, m = map(int, input().split())
line1 = []
vert = []

for l in range(m):
    line1.append("#")

for v in range(n):
    if v%2 == 0:
        for i in range(m-1):
            vert.append('.')
        vert.append("#")
    else:
        for i in range