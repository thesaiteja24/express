''' Given two strings s and t, return   true   if   t   is   an   anagram   of   s, and false otherwise.


An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram" Output: true
Example 2:
Input: s = "rat", t = "car" Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
'''


def isAnagram(s, t):
    return sorted(s) == sorted(t)


testCase1 = ("anagram", "nagaram")
testCase2 = ("rat", "car")

print(isAnagram(testCase1[0], testCase1[1]))
print(isAnagram(testCase2[0], testCase2[1]))