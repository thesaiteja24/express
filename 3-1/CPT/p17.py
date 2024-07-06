'''
Given an integer array nums, return the third distinct maximum number in this     array.     If     the     third     maximum     does     not     exist,     return the maximum number.

Example 1:
Input: nums = [3,2,1] Output: 1 Explanation:
The first distinct maximum is 3. The second distinct maximum is 2. The third distinct maximum is 1.
Example 2:
Input: nums = [1,2] Output: 2 Explanation:
The first distinct maximum is 2. The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned
'''

def bigThree(lis):
    lis = sorted(set(lis))
    if len(lis) < 3:
        return lis[-1]
    else:
        return lis[-3]
testCase1 = [3,2,1]
testCase2 = [1,2]
testCase3 = [12, 13, 1, 10, 34, 16]
testCase4 = [2, 2, 3, 1]

print(bigThree(testCase1))
print(bigThree(testCase2))
print(bigThree(testCase3))
print(bigThree(testCase4))