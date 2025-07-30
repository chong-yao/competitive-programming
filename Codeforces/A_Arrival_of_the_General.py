n = int(input())
heights = [int(x) for x in input().split()]

tallest = heights.index(max(heights))
shortest = len(heights) - 1 - heights[::-1].index(min(heights))

moves = tallest + (n - 1 - shortest)

if tallest > shortest:
    moves -= 1

print(moves)