import itertools
f = open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\Sum^k.txt", "r")
nums = [int(x) for x in f.read().split()]
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

s = nums
ans = []
j = 1
for i in range(len(s)):
    ans.append(findsubsets(s, j))
    j+=1

print(ans)