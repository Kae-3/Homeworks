def sieve_two_digit_primes(limit: int = 99):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    crossings = 0

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            # Start marking multiples from p*p since smaller multiples were already handled
            for multiple in range(p * p, limit + 1, p):
                crossings += 1
                if is_prime[multiple]:
                    is_prime[multiple] = False
        p += 1

    two_digit_primes = [num for num in range(10, limit + 1) if is_prime[num]]
    return two_digit_primes, crossings


primes, total_crossings = sieve_two_digit_primes(99)
print("Two-digit primes (10-99):", primes)
print("Count of two-digit primes:", len(primes))
print("Total sieve crossings:", total_crossings)