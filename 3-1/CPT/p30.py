'''
John has a string S with him. John is happy if the string contains a contiguous substring of length strictly greater than 22 in which all its characters are vowels.

Determine whether John is happy or not.
Note that, in english alphabet, vowels are a, e, i, o, and u.
Input Format
First line will contain T, number of test cases. Then the test cases follow. Each test case contains of a single line of input, a string S.
Output Format
For each test case, if John is happy, print HAPPY else print SAD.
You may print each character of the string in uppercase or lowercase (for example, the strings hAppY, Happy, haPpY, and HAPPY will all be treated as identical).
Constraints
1≤T≤1000
3≤∣S∣≤1000, where ∣S∣ is the length of S. S will only contain lowercase English letters.

Input: 4	Output:
Aeiou	Happy
Abxy	Sad
Aebcdefghij	Sad
Abcdeeafg	Happy
'''
T = int(input())
lis = []
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(T):
    s = input()
    ans = ""
    for i in range(len(s)-1):
        if s[i] in vowels and s[i+1] in vowels and s[i+2] in vowels:
            ans = "HAPPY"
            break
        else:
            ans = "SAD"
    lis.append(ans)
for i in lis:
    print(i)