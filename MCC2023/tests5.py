f = open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\Sum^k.txt", "r")
MOD = 998244353

n, k = [int(i) for i in f.readline().split()]
nums = [int(i) for i in f.readline().split()]

sums = [0]
result = 0

for i in range(1, n):
    sums[0] += nums[i]

for i in range(1, n):
    sums.append(sums[i-1] - nums[i])

def solve_sum():
    index = 0
    for x in nums:
        result = (result + pow(x, k) * pow(2, n-1, MOD)) % MOD

print(result)