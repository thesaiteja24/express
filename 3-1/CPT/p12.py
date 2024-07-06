'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad" Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:
Input: haystack = "PythonCode", needle = "Pythoc" Output: -1
Explanation: "Pythoc" did not occur in "PythonCode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
'''


def needeHaystack(haystack, needle):
    return haystack.find(needle)
        

testCase1 = ("sadbutsad", "sad")
testCase2 = ("PythonCode", "Pythoc")

print(needeHaystack(testCase1[0], testCase1[1]))
print(needeHaystack(testCase2[0], testCase2[1]))
