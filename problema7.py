def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    
    # Collecting all prime numbers less than or equal to 'limit'
    prime_numbers = []
    for p in range(2, limit + 1):
        if primes[p]:
            prime_numbers.append(p)
    
    return prime_numbers

def find_nth_prime(n):
    # Estimate the upper bound using the Prime Number Theorem
    # log(n) * (log(log(n))) gives a good estimate for n-th prime
    import math
    limit = int(math.log(n) * math.log(math.log(n)))
    while True:
        primes = sieve_of_eratosthenes(limit)
        if len(primes) >= n:
            return primes[n - 1]
        limit *= 2

# Find the 10,001st prime number
nth_prime = find_nth_prime(10_001)

print(f"The 10,001st prime number is: {nth_prime}")
