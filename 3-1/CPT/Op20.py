'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab" Output: true
Explanation: It is the substring "ab" twice.
Example 2:
Input: s = "aba" Output: false Example 3:
Input: s = "abcabcabcabc" Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
'''


def is_repeated_substring_pattern(s: str) -> bool:
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            substring = s[:i]
            if substring * (n // i) == s:
                return True
    return False


testCase1 = "abab"
testCase2 = "aba"
testCase3 = "abcabcabcabc"

print(is_repeated_substring_pattern(testCase1))
print(is_repeated_substring_pattern(testCase2))
print(is_repeated_substring_pattern(testCase3))
