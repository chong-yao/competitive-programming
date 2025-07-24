MOD = 998244353

def solve(n, k, s):
    # Reduce k modulo (MOD-1) to handle large exponents
    k = k % (MOD - 1)

    # Precompute the modular inverse of 3
    inv3 = pow(3, MOD - 2, MOD)

    # Precompute 2^k % MOD
    pow2k = pow(2, k, MOD)

    # Compute (-1)^k modulo MOD
    if k % 2 == 0:
        minus_one_pow_k = 1
    else:
        minus_one_pow_k = MOD - 1  # Since -1 % MOD = MOD - 1

    # Compute beauty values using modular arithmetic

    # For '11'
    numerator_11 = (pow2k + 2 * minus_one_pow_k) % MOD
    beauty_11 = (numerator_11 * inv3) % MOD

    # For '01' and '10'
    numerator_01 = (pow2k - minus_one_pow_k + MOD) % MOD  # Ensure non-negative
    beauty_01 = (numerator_01 * inv3) % MOD

    # For '00'
    beauty_00 = pow2k % MOD

    arr = []
    for i in range(1, n):
        tmp = s[i - 1] + s[i]
        if tmp == '00':
            arr.append(beauty_00)
        elif tmp == '11':
            arr.append(beauty_11)
        else:
            arr.append(beauty_01)

    n -= 1  # Adjust n since we're dealing with adjacent pairs
    ans = 0
    for i in range(n):
        contrib = arr[i] * (n - i) * (i + 1)
        ans = (ans + contrib) % MOD

    return ans

with open('input.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    s = file.readline().strip()

# Calculating the result
result = solve(n, k, s)

# Output the result to 'output.txt'
with open('output.txt', 'w') as file:
    file.write(str(result) + "\n")
