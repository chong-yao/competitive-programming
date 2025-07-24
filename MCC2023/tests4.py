MOD = 998244353
f = open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\Sum^k.txt", "r")
nums = [int(x) for x in f.read().split()]
def solve(N, K, A):
    ans = 0
    for i in range(1, 2**N):
        s = 0
        for j in range(N):
            if i & (1<<j):
                s += A[j]
        ans += pow(s, K, MOD)
    return ans % MOD

N = 100000
K = 2
A = nums
print(solve(N, K, A))