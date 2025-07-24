ans = 0
subsetsum = []
f = open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\Sum^k.txt", "r")
nums = [int(x) for x in f.read().split()]
k = 200

def calcSubset(A, res, subset, index):
    # Add the current subset to the result list
    res.append(subset[:])
 
    # Generate subsets by recursively including and excluding elements
    for i in range(index, len(A)):
        # Include the current element in the subset
        subset.append(A[i])
 
        # Recursively generate subsets with the current element included
        calcSubset(A, res, subset, i + 1)
 
        # Exclude the current element from the subset (backtracking)
        subset.pop()
 
 
def subsets(A):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index)
    return res

res = subsets(nums)
print(res)
# Print the generated subsets
for subset in res:
    subsetsum.append(pow(sum(subset), k, 998244353))

print(sum(subsetsum))