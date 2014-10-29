import math

def is_prime(n):
    if n < 0:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n%j == 0:
            return False
    return True

def divisors(n):
        count = 1
        divisors = []
        for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                        divisors.append(i)
                        divisors.append(n/i)
        divisors = list(set(divisors))
        return sorted(divisors)
