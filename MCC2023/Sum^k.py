# # n, k = map(int, input().split())
# # nums = [int(x) for x in input().split()]
# ans = 0

# f = open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\Sum^k.txt", "r")
# nums = {int(x) for x in f.read().split()}
# # h = open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\sumktxt", "w")
# # h.write(str(nums))
# def powerset(s):
#     x = len(s)
#     masks = [1 << i for i in range(x)]
#     for i in range(1 << x):
#         yield [ss for mask, ss in zip(masks, s) if i & mask]

# subsets = list(powerset(nums))
# print(subsets)
# for i in subsets:
#     ans += sum(i)**2
    
# print(ans)

n, k = map(int, input().split())
nums = [int(x) for x in input().split()]
ans = []

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

subsets = list(powerset(nums))
for i in subsets:
    currentsum = sum(i)
    ans.append(currentsum**k)
    
print(sum(ans)%998244353)