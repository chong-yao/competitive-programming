def can_destroy_all_targets(n, m, k, a, x):
    remaining_hp = a[:]  # Copy of the original HP values
    arrows_used = 0

    i = 0
    while i < n:
        if remaining_hp[i] > 0:
            if arrows_used == k:
                return False  # No more arrows left
            arrows_used += 1

            # Apply damage from arrow shot at target i
            for j in range(i, n):
                if remaining_hp[j] > 0:
                    damage = max(0, m * x - (j - i) ** 2)
                    if damage == 0:
                        break  # No further damage
                    remaining_hp[j] -= damage

        # Move to the next target with positive HP
        while i < n and remaining_hp[i] <= 0:
            i += 1

    return True

def find_minimum_x(n, m, k, a):
    low, high = 1, 999999999999999999999999999999999999999999999999999999999999
    final = high

    while high >= low:
        mid = (high + low) // 2
        if can_destroy_all_targets(n, m, k, a, mid):
            final = mid
            high = mid - 1  # Try to find a smaller x
        else:
            low = mid + 1  # Try to find a larger x

    return final

# Read input from input.txt
with open('input.txt', 'r') as fin:
    # Reading values of n, m, k
    n, m, k = map(int, fin.readline().split())
    # Reading the list of HP values for the targets
    a = list(map(int, fin.readline().split()))

# Find the minimum x
result = find_minimum_x(n, m, k, a)

# Write output to output.txt
with open('output.txt', 'w') as fout:
    fout.write(f"{result}\n")
