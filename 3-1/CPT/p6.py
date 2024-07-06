def isPalindrome(s):
    return str(s) == str(s)[::-1]
print(isPalindrome(121))
print(isPalindrome(-121))