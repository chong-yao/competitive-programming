n = int(input())

points = [int(x) for x in input().split()]

minpoint, maxpoint = points[0], points[0]

ans = 0

for i in points[1:]:
    if i > maxpoint:
        maxpoint = i
        ans+=1

    elif i < minpoint:
        minpoint = i
        ans+=1

print(ans)