n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    if y == x + 1 or (x > y and (x - y + 1)%9 ==0):
        print("Yes")

    else:
        print("No")