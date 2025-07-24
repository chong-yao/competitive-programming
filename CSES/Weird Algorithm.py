n = int(input())
ans = []
ans.append(int(n))
while n!=1:
    if n % 2 == 0:
        ans.append(int(n/2))
        n = int(n/2)
    else:
        ans.append(int(n*3 + 1))
        n = int(n*3 + 1)

print(*ans, sep = ' ')