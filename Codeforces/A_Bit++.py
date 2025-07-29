operations = input()
i = 0
for j in range(int(operations)):
    line = input()
    if "++" in line:
        i = i + 1
    elif "--" in line:
        i = i - 1

print(i)