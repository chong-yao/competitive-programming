line1 = input()
line2 = input()
line3 = input()

if sorted(line1 + line2) == sorted(line3):
    print("YES")
else:
    print("NO")