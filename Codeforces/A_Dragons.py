s, n = map(int, input().split())

dragons = []
dragonhealth = []
dragonbonus = []

ans = True

for i in range(n):
    x, y = map(int, input().split())
    dragonhealth.append(x)
    dragonbonus.append(y)

for j in dragonhealth:
    if j < s:
        s += dragonbonus[dragonhealth.index(j)]

for x in dragonhealth:
    if j > s:
        ans = False
        break

if ans:
    print("YES")

else: print("NO")