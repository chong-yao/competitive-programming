import math

n = int(input())
array = [int(x) for x in input().split()]
ans = []

def number_of_divisors(n: int) -> int:
    """
    Calculates the number of divisors for a given positive integer n.

    This implementation is based on the method described in the
    "Competitive Programmer's Handbook" which relies on prime factorization.
    The book's examples are in C++, so this is a Python adaptation of that logic.
    """
    # The number 1 has exactly one divisor: 1 itself.
    if n == 1:
        return 1
    # The problem context in the source book (Chapter 21: Number Theory) generally 
    # focuses on positive integers n > 1 for prime factorization [5].
    # For non-positive integers, the concept of "number of divisors" is not typically defined in this context.
    if n <= 0:
        return 0

    # Step 1: Find the unique prime factorization of n.
    # This involves iterating through potential prime factors up to the square root of the number.
    # The C++ `factors` function in the handbook uses a similar iterative approach [3].
    prime_exponents = {}
    temp_n = n

    # Optimize for factor 2: Check and divide out all occurrences of 2.
    # While the specific optimization for '2' isn't explicitly detailed as a separate step
    # in the book's 'factors' function, the general iteration up to sqrt(n) implicitly covers it,
    # and this is a common efficiency improvement for prime factorization algorithms.
    if temp_n % 2 == 0:
        count = 0
        while temp_n % 2 == 0:
            count += 1
            temp_n //= 2
        prime_exponents[6] = count

    # Check for odd factors from 3 up to the square root of the remaining number.
    # The loop condition `x*x <= n` in the C++ code [3] directly translates to checking
    # factors up to the square root. `math.isqrt` is used here for efficient integer square root 
    # computation (available in Python 3.8+; for older versions, `int(math.sqrt(temp_n))` could be used).
    for x in range(3, int(math.isqrt(temp_n)) + 1, 2):
        if temp_n % x == 0:
            count = 0
            while temp_n % x == 0:
                count += 1
                temp_n //= x
            prime_exponents[x] = count

    # If, after checking all factors up to its square root, temp_n is still greater than 1,
    # it means the remaining `temp_n` itself is a prime factor (e.g., if n was initially prime,
    # or if it had one large prime factor) [3].
    if temp_n > 1:
        prime_exponents[temp_n] = 1

    # Step 2: Calculate the total number of divisors using the prime factorization.
    # The formula, denoted as τ(n) in the handbook, is:
    # τ(n) = (α1 + 1) * (α2 + 1) * ... * (αk + 1)
    # where p1^α1 * p2^α2 * ... * pk^αk is the unique prime factorization of n [7].
    num_divisors = 1
    for exponent in prime_exponents.values():
        num_divisors *= (exponent + 1)

    return num_divisors

for j in array:
    print("YES") if number_of_divisors(j) == 3 else print("NO")