def distribute_gifts(n, m, tiers):
    # Pair guests with their indices (order of arrival)
    guests = [(tier, i) for i, tier in enumerate(tiers)]
    # Sort by tier then by order of arrival
    guests.sort()

    # Result array: all initially set to 0
    result = [0] * n

    # Give out the gifts
    for tier, index in guests:
        if m == 0:  # All gifts finished
            break
        result[index] = 1
        m -= 1

    return result

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    n, m = map(int, lines[0].split())
    tiers = list(map(int, lines[1].split()))

output = distribute_gifts(n, m, tiers)

with open("output.txt", "w") as output_file:
    output_file.write(" ".join(map(str, output)))