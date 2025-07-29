n = int(input())
ans = 0
for i in range(n):
    p, q = map(int, input().split())
    if q - p - 2 >= 0:
        ans+=1
print(ans)