def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=' ', flush=True)
    print()


n = 7
if isprime(n):
    print(f'{n} is a prime number')
    print()
else:
    print(f'{n} is not a prime number')
    print()

print('First 100 prime numbers are:')
list_primes()
