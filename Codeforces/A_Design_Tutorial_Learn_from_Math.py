n = int(input())

if n % 2 == 0:
    print(8, n - 8)
else:
    print(9, n - 9)

# Because for n >= 12:
# subtracting 8 from an even n leaves an even number >= 4
# subtracting 9 from an odd n leaves an even number >= 4

# since all even numbers ≥ 4 are composite, each constructed value will be composite by definition