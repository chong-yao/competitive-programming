t = int(input())

for i in range(t):
    ticket = [int(x) for x in input()]

    print("YES") if sum(ticket[0:3]) == sum(ticket[3:6]) else print("NO")