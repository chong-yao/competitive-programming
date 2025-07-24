n, k = map(int, input().split())
cards = sorted([int(x) for x in input().split()])
ans = 0
error = 0

for i in range(len(cards)-1):
    if cards[i] + 1 == cards[i+1]:
        ans+=1
    else:
        error += 1

print(ans, error)