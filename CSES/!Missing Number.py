#nf
n = int(input())
num = sorted(list(int(x) for x in input().split()))

for i in range(1, len(num)+1):
    if i not in num:
        print(i)