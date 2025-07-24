t = int(input())
ans = []
for _ in range(t):
    n, a, b = map(int, input().split())
    enemylvl = list(map(int, input().split()))
    enemylvl.sort()
    count = 0
    check = True
    while a < b and len(enemylvl) > 0:
        i = 0
        while i < len(enemylvl) and enemylvl[i] < a:
            i += 1
        i -= 1
        if i == -1:
            check = False
            break
        a += enemylvl[i]
        enemylvl.pop(i)
        count += 1
    if not check:
        ans.append(-1)
        continue
    if a < b:
        ans.append(-1)
    else:
        ans.append(count)

print(*ans, sep='\n')