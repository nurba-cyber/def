def printMatrix(n, m):
    num = 1
    for i in range(n):
        for j in range(m):
            print(num, end=" ")
            num += 1
        print()  

printMatrix(2, 3)
