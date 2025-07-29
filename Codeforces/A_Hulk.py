n = int(input())

output = []

for i in range(n):
    if i%2 == 0:
        output.append("I hate")

    else:
        output.append("I love")

text_to_insert = ' that '

output = text_to_insert.join(output)
print(output, "it")