#Codeforces A. Next Round
n, k = map(int, input().split())
scores = list(map(int, input().split()))
ans = 0
for i in range(n):
    test = scores[i]
    if int(test) >= scores[k-1] and int(test) !=0:
        ans += 1
    else:
        break

print(ans)