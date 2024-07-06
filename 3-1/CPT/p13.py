'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5 Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2 Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7 Output: 4

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
'''

def returnIndex(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return left

testCase1 = ([1,3,5,6],5)
testCase2 = ([1,3,5,6],2)
testCase3 = ([1,3,5,6],7)

print(returnIndex(testCase1[0], testCase1[1]))
print(returnIndex(testCase2[0], testCase2[1]))
print(returnIndex(testCase3[0], testCase3[1]))