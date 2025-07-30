n = int(input())
a = [int(x) for x in input().split()]

max_days = 1
current_days = 1

for i in range(1, n):
    if a[i] >= a[i-1]:
        current_days +=1
    
    else:
        current_days = 1
    
    if current_days > max_days:
        max_days = current_days

print(max_days)