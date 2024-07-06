'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1: Input: n = 1 Output: true
Explanation: 2^0 = 1
Example 2: Input: n = 16 Output: true
Explanation: 2^4 = 16
Example 3: Input: n = 3 Output: false

Constraints:
-2^31 <= n <= 2^31 - 1
'''

def isPowerOfTwo(n):
    if n < 1:
        return False
    return (n & (n - 1)) == 0

testCase1 = 6

print(isPowerOfTwo(testCase1))
