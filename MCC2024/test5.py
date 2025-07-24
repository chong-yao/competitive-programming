MOD = 998244353

def solve(n, k, s):
    # Reduce k modulo (MOD-1) to handle large exponents
    k = k % (MOD - 1)

    arr = []

    # Precompute the modular exponentiation of 2^k % MOD
    power_of_2_k = pow(2, k, MOD)

    for i in range(1, n):
        tmp = s[i-1] + s[i]
        
        if tmp == "00":
            arr.append(power_of_2_k)  # 2^k % MOD
        elif tmp == "11":
            # Using modular arithmetic for division and handling negative numbers correctly
            arr.append((((power_of_2_k) + 2 * ((-1)**k)) % MOD * pow(3, MOD-2, MOD)) % MOD)
        else:
            # Calculate (2^k + 1) // 3 % MOD
            arr.append(((power_of_2_k + 1) // 3) % MOD)
    
    n -= 1
    ans = 0
    for i in range(n):
        ans += arr[i] * (n - i) * (i + 1)
        ans %= MOD

    return ans

# Reading input from 'input.txt'
with open('input.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    s = file.readline().strip()

# Calculating the result
result = solve(n, k, s)

# Output the result to 'output.txt'
with open('output.txt', 'w') as file:
    file.write(str(result) + "\n")