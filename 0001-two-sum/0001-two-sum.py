class Solution(object):
    def twoSum(self, nums, target):
        h = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in h:
                return (i, h[rem])
            h[nums[i]] = i