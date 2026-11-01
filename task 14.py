def transformDigits(n):
    res = ""
    for d in str(n):
        d = int(d)
        if d % 2 == 0:
            res += str(d + 1)
        else:
            res += str(d - 1)
    return int(res)

N = 983210
print("Output =", transformDigits(N))
