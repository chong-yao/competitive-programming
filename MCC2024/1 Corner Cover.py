# Open the input file and read data
with open('input.txt', 'r') as f:
    t = int(f.readline())
    results = []

    def can_cover_two_corners(n, m, a, b):
        if (a == n and b <= m) or (a <= n and b == m) or (b == n and a <= m) or (b <= n and a == m):
            return "YES"
        return "NO"

    for _ in range(t):
        # Read the values for each test case
        n, m, a, b = map(int, f.readline().split())

        # Process the test case and store the result
        result = can_cover_two_corners(n, m, a, b)
        results.append(result)

# Open the output file and write the results
with open('output.txt', 'w') as f:
    for res in results:
        f.write(res + '\n')