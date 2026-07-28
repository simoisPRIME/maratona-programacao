class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                soma = nums[i] + nums[j]
                if (soma == target):
                    return [i, j]  