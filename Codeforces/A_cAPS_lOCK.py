x = input()

if x == x.upper() or (x[0] == x[0].lower() and x[1:] == x[1:].upper()):
    print(x.swapcase())

else:
    print(x)