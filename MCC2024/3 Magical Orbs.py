MOD = 10**9 + 7

# Open the input file and read data
with open('input.txt', 'r') as f:
    t = int(f.readline())
    results = []

    for _ in range(t):
        n = int(f.readline())
        powers = list(map(int, f.readline().split()))
        powers.sort(reverse=False)

        while len(powers) > 1:
            y = powers.pop()
            x = powers.pop()

            powers.append(x + 2 * y)

            # Re-sort to maintain the two largest at the end
            powers.sort(reverse=False)

        results.append(powers[0] % MOD)

with open('output.txt', 'w') as f:
    for res in results:
        f.write(str(res) + '\n')
