import itertools
list1 = []
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

p = int(input())
k = int(input())

for i in range(p, k+1):
    list1.append(i)

ans = []
j = 1
for i in range(len(list1)):
    ans.append(findsubsets(list1, j))
    j+=1

print(ans)