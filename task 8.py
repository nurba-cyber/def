def decimalToBinary(n):
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res

N = 13
print("Binary =", decimalToBinary(N))
