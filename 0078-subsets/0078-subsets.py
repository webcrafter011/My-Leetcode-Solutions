class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for mask in range(2 ** n):
            subset = []

            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            
            res.append(subset)
        
        return res