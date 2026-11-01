def printInvertedPyramid(n):
    for i in range(n, 0, -1):
        d = '' * (n - i)
        c = '*' * (2 * i - 1)
        print(d + c)

printInvertedPyramid(3)
