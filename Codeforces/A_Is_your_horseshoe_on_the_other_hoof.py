shoes = list(map(int, input().split()))

unique_shoes = list(set(shoes))

print(4 - len(unique_shoes))