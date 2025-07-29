n = int(input())
axis0 = 0
axis1 = 0
axis2 = 0

for i in range(n):
    cur = input().split()
    axis0 += int(cur[0])
    axis1 += int(cur[1])
    axis2 += int(cur[2])

print("NO" if axis0 or axis1 or axis2 !=0 else "YES")