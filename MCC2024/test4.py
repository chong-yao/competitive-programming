MOD = 998244353

def solve(n, k, s):
    # Reduce k modulo (MOD-1) to avoid overflows
    k = k % (MOD - 1)

    arr = []
    # Precompute 2^k % MOD for large k
    power_of_2_k = pow(2, k, MOD)

    # Calculate the transformation effects for each adjacent pair in the string
    for i in range(1, n):
        tmp = s[i-1] + s[i]
        
        if tmp == "00":
            arr.append(power_of_2_k)  # 2^k % MOD for "00"
        elif tmp == "11":
            # Special case for "11", where the transformation is complex
            arr.append((((power_of_2_k) + 2 * ((-1)**k)) % MOD * pow(3, MOD-2, MOD)) % MOD)
        else:
            # Special case for "01" or "10"
            arr.append(((power_of_2_k + 1) // 3) % MOD)
    
    # Now we will calculate the final result using the computed array
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
