class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        maxi = max(nums)

        for num in nums:
            res += maxi - num
        
        return res
        
