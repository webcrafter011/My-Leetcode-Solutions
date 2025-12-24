from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def solve(i, summ):
            if i == 0:
                count = 0
                if (nums[i] + summ) == target:
                    count += 1
                if (summ - nums[i]) == target:
                    count += 1
                return count
            
            add = solve(i - 1, summ + nums[i])
            remove = solve(i - 1, summ - nums[i])

            return add + remove
        
        n = len(nums)
        return solve(n - 1, 0)