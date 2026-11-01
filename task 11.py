def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = 6
b = 8
print("LCM =", lcm(a, b))
