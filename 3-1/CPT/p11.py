'''
Given	a	non-empty	array	of	integers	nums,	every	element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1] Output: 1
Example 2:
Input: nums = [4,1,2,1,2] Output: 4
Example 3:
Input: nums = [1] Output: 1

Constraints:
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4 
Each element in the array appears twice except for one element which appears only once

Logic:
To solve this problem with a linear runtime complexity and constant extra space, we can use the XOR (exclusive OR) operation. The XOR operation has the following properties:
a ^ 0 = a
a ^ a = 0
a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
'''


def uniqueNum(nums):
    result = 0
    for num in nums:
        result = result ^ num
    return result

testCase1 = [2,2,1]
testCase2 = [4,1,2,1,2] 
testCase3 = [1]

print(uniqueNum(testCase1))
print(uniqueNum(testCase2))
print(uniqueNum(testCase3))