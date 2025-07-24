MOD = 998244353

def solve(n, k, s):
    # Reduce k modulo (MOD-1) to handle large exponents in modular arithmetic
    k = k % (MOD - 1)

    # Precompute the modular exponentiation of 2^k % MOD
    power_of_2_k = pow(2, k, MOD)

    # Array to store results for each pair of consecutive characters
    arr = []

    # Precompute the values for each pair of adjacent characters in the string
    for i in range(1, n):
        pair = s[i-1] + s[i]
        
        if pair == "00":
            # Case "00": The result is 2^k % MOD
            arr.append(power_of_2_k)
        elif pair == "11":
            # Case "11": Modular arithmetic with handling for division
            # We use (-1)^k to alternate between adding and subtracting based on k
            sign = 1 if k % 2 == 0 else MOD - 1  # (-1)^k modulo MOD
            arr.append(((power_of_2_k + 2 * sign) % MOD * pow(3, MOD - 2, MOD)) % MOD)
        else:
            # Case "01" or "10": Calculate (2^k + 1) // 3 % MOD
            arr.append(((power_of_2_k + 1) * pow(3, MOD - 2, MOD)) % MOD)

    # Calculating the weighted sum of the precomputed values
    ans = 0
    for i in range(n - 1):
        ans += arr[i] * (n - i - 1) * (i + 1)
        ans %= MOD

    return ans

# Reading input
n, k = map(int, input().split())
s = input().strip()

# Calculating the result
result = solve(n, k, s)
print(result)