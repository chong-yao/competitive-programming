n = int(input())

dict = {}

for i in range(n):
    x = input()
    if x not in dict:
        dict[x] = 0
        print("OK")

    else:
        dict[x] += 1
        print(x + str(dict[x]))