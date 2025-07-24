MOD = 998244353

def solve(n, k, s):
    # Reduce k modulo (MOD-1) for large exponents
    k %= (MOD - 1)

    # Precompute the modular inverse of 3
    inv3 = pow(3, MOD - 2, MOD)

    # Precompute 2^k % MOD
    pow2k = pow(2, k, MOD)

    # Compute (-1)^k modulo MOD
    minus_one_pow_k = 1 if k % 2 == 0 else MOD - 1

    # Precompute beauty values
    beauty_00 = pow2k % MOD
    beauty_11 = ((pow2k + 2 * minus_one_pow_k) % MOD * inv3) % MOD
    beauty_01 = ((pow2k - minus_one_pow_k + MOD) % MOD * inv3) % MOD

    arr = []
    for i in range(1, n):
        pair = s[i - 1] + s[i]
        if pair == '00':
            arr.append(beauty_00)
        elif pair == '11':
            arr.append(beauty_11)
        else:
            arr.append(beauty_01)

    # Calculate the final result
    ans = 0
    for i in range(n - 1):
        ans = (ans + arr[i] * (n - i - 1) * (i + 1)) % MOD

    return ans

# Read input from 'input.txt'
with open('input.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    s = file.readline().strip()

# Calculate the result
result = solve(n, k, s)

# Output the result to 'output.txt'
with open('output.txt', 'w') as file:
    file.write(f"{result}\n")
