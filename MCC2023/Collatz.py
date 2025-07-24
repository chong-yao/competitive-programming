n, k = map(int, input().split())
nums = input().split()
num = [int(x) for x in nums]

for i in range(k):
    for i in range(n):
        if num[i] % 2 == 0:
            num[i] = num[i]/2
        else:
            num[i] = 3*num[i] + 1

print(int(sum(num)))