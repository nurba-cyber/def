def isPalindrome(n):
    t= n
    r= 0
    while t > 0:
        rev = r * 10 + t% 10
        t //= 10
    return r == n

N = 121
if isPalindrome(N):
    print("Palindrome")
else:
    print("Not Palindrome")
