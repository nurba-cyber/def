def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def countPrimes(a, b):
    c = 0
    for num in range(a, b + 1):
        if isPrime(num):
            c += 1
    return c

A = 10
B = 30
print("Prime Count =", countPrimes(A, B))
