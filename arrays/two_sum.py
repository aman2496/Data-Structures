'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Reason: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def two_sum(nums, target):
    output = []
    lookUp = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in lookUp.keys():
            second_idx = nums.index(complement)

            if i != second_idx:
                return sorted([i, second_idx])
        lookUp.update({nums[i] : i})

nums = [2,7,11,15]
target = 9

output = two_sum(nums, target)
print(output)
