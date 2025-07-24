mod = 998244353

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

ttl = sum(a)
coeff = pow(2, n-1, mod)

result = 0
for i in a
    ttl -= i