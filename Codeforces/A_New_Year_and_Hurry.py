n, k = map(int, input().split())

remaining_time = 240 - k
time_spent = 0
solved_count = 0

for i in range(1, n+1):
    time_spent += 5*i
    if time_spent <= remaining_time:
        solved_count += 1
    
    else:
        break

print(solved_count)