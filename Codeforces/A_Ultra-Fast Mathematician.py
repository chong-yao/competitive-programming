line1 = list(int(x) for x in input())
line2 = list(int(x) for x in input())
ans = []
for i in range(len(line1)):
    if line1[i] != line2[i]:
        ans.append("1")
    else:
        ans.append("0")
print(''.join(ans))