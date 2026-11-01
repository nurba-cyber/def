def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = 24
b = 36
print("GCD =", gcd(a, b))
