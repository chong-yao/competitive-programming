l, b = map(int, input().split())
ans = 0

if l > b:
    ans = 0
else:
    while l <= b:
         l = l*3
         b = b*2
         ans +=1

print(ans)