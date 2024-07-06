# Two sum
def twoSum(nums, target):
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if nums[i]+nums[j] == target:
                print([i, j])



twoSum([2, 7, 11, 15], 9)


def twoSumV2(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []
