t = int(input())
ans = []
for i in range(t):
    n = int(input())
    if n>2:
        if n%2 == 0:
            ans.append(int(n/2)-1)
        else:
            ans.append(int(n/2))
    else:
        ans.append(0)
        
print(*ans, sep = '\n')