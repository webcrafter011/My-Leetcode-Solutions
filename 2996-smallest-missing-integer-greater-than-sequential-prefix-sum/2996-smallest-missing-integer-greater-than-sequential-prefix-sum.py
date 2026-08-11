class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        long_presum = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                long_presum += nums[i]
            else:
                break
        
        nums = set(nums)

        while long_presum in nums:
            long_presum += 1
        
        return long_presum
                