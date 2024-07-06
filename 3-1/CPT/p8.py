testCase1 = "A man, a plan, a canal: Panama"
testCase2 = "race a car"
testCase3 = ""


def isPalindrome(s):
    s = s.replace(" ","")
    s = s.replace(",", "")
    s = s.replace(":", "")
    print(s)
    return s.lower() == s[::-1].lower()

print(isPalindrome(testCase1))