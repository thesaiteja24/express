def addStrings(num1, num2):
    n1 = len(num1) - 1
    n2 = len(num2) - 1
    carry = 0
    ans = []
    while n1 >= 0 or n2 >= 0:
        if n1 < 0:
            ans.append(str((int(num2[n2]) + carry) % 10))
            carry = (int(num2[n2]) + carry) // 10
            n2 -= 1
        elif n2 < 0:
            ans.append(str((int(num1[n1]) + carry) % 10))
            carry = (int(num1[n1]) + carry) // 10
            n1 -= 1
        else:
            ans.append(str(((int(num1[n1]) + int(num2[n2]) + carry) % 10)))
            carry = ((int(num1[n1]) + int(num2[n2]) + carry) // 10)
            n1 -= 1
            n2 -= 1
    if carry:
        ans.append(str(carry))
    ans.reverse()
    return ''.join(ans)


testCase1 = ("11", "123")
testCase2 = ("456", "77")
testCase3 = ("0", "0")

print(addStrings(testCase1[0], testCase1[1]))
print(addStrings(testCase2[0], testCase2[1]))
print(addStrings(testCase3[0], testCase3[1]))