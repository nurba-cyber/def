def isArmstrong(n):
    t = n
    s = 0
    while t > 0:
        d = t % 10
        s += d**3
        t //= 10
    return s == n

for i in range(100, 1000):
    if isArmstrong(i):
        print(i, end=" ")
