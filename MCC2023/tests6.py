f = open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\Sum^k.txt", "r")
MOD = 998244353

n, k = [int(i) for i in f.readline().split()]
a = [int(i) for i in f.readline().split()]

sums = [0]
for i in range(1, n):
    sums[0] += a[i] * (k-1)

for i in range(1, n):
    sums.append(sums[i-1] - a[i])

def solve_sum():
    result = 0
    index = 0
    for x in a: 
        result = (result + pow(x, k) * pow(2, n-1, MOD)) % MOD
        result = (result + pow(2, n-1, MOD) * x * sums[index]) % MOD

        index += 1
    return result

print(solve_sum())