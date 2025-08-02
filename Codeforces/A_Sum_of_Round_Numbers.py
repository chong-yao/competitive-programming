t = int(input()) # Number of test cases

for i in range(t):
    n = int(input())
    round_numbers = []
    consecutive_zeros = 0

    while n > 0:
        digit = n % 10
        if digit != 0:
            round_numbers.append(digit * 10**consecutive_zeros)
        n = n // 10
        consecutive_zeros += 1

    print(len(round_numbers))
    print(*round_numbers)