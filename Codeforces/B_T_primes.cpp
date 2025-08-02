#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>

// Function to check if a number is prime
bool isPrime(long long n) {
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false;
    }
    for (long long i = 5; i * i <= n; i = i + 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

// Function to check if a number has exactly three divisors
void hasThreeDivisors(long long n) {
    if (n <= 0) {
        std::cout << "NO" << std::endl;
        return;
    }
    long long root = round(sqrt(n));
    if (root * root == n && isPrime(root)) {
        std::cout << "YES" << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n;
    std::cin >> n;
    std::vector<long long> array(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> array[i];
    }

    for (long long j : array) {
        hasThreeDivisors(j);
    }

    return 0;
}