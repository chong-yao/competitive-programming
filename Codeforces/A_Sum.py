t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())

    if (a == b + c) or (b == a + c) or (c == a + b):
        print("YES")
    else:
        print("NO")