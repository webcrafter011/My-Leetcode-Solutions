class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        i = 1
        num = k
        while num in nums:
            num = k * i
            i += 1
        
        return num