class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = 1
        si = sd = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                si += 1
                inc = max(inc, si)
            else:
                si = 1

            if nums[i] < nums[i - 1]:
                sd += 1
                dec = max(dec, sd)
            else:
                sd = 1
        
        return max(inc, dec)
        
