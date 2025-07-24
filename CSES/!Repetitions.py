n = sorted(list(input()))
ans = []
for i in range(len(n)):
    ans.append(n.count(n[i]))

print(max(ans))