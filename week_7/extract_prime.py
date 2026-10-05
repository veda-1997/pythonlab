def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


numbers = range(1, 51)

primes = list(filter(is_prime, numbers))

print("Prime numbers:", primes)

# Output:
# Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
