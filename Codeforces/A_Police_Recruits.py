n = int(input())

activity = [int(x) for x in input().split()]

cops = 0
crime = 0
ans = 0

for i in activity:
    if i == 1:
        cops += 1

    else:
        if cops:
            cops -= 1
        
        else:
            crime += 1


print(cops, crime)