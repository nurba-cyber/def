def reverseNumber(n):
    r = 0
    while n > 0:
        rev = r * 10 + n % 10
        n //= 10
    return r

N = 1234
print("Output =", reverseNumber(N))
