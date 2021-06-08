
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0  or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def primes_upto(limit):
    result = [num for num in range(2, limit) if isPrime(num)]
    return result

print(primes_upto(12))



