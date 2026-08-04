class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        nums = set(nums)
        res = []

        for i in range(small, large + 1):
            if i not in nums:
                res.append(i)
        
        return res