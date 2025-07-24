def game_result(n, pairs):
    # Step 1: Sort the pairs by (ai + bi) in descending order
    pairs.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    # Step 2: Initialize scores for both players
    X = 0  # Evirir's score
    Y = 0  # Rhae's score
    
    # Step 3: Alternate picking the pairs
    for i in range(n):
        ai, bi = pairs[i]
        if i % 2 == 0:  # Evirir's turn (Evirir picks ai)
            X += ai
        else:           # Rhae's turn (Rhae picks bi)
            Y += bi
    
    # Step 4: Calculate the final score difference (X - Y)
    return X - Y

# Reading input from input.txt
with open("input.txt", "r") as infile:
    n = int(infile.readline())  # Read number of pairs
    pairs = [tuple(map(int, infile.readline().split())) for _ in range(n)]

# Compute the result
result = game_result(n, pairs)

# Writing the result to output.txt
with open("output.txt", "w") as outfile:
    outfile.write(f"{result}\n")
