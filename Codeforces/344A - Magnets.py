#time limit exceeded

n = int(input())
ans = 1
mag = []
for i in range(n):
    mag.append(input())

for j in range(n-1):
    if mag[j] != mag[j+1]:
        ans+=1
print(ans)