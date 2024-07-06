'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"] Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"] Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''


def longestCommonPrefix(strs):
    lcp = ""
    star = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return lcp
        lcp += first[i]
    return lcp


testCase1 = ["flower", "flow", "flight"]
testCase2 = ["dog", "racecar", "car"]

print(longestCommonPrefix(testCase1))
print(longestCommonPrefix(testCase2))
