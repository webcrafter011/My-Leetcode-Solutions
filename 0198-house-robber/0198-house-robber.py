class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. Recursion solution (includes stack space extra O(n))
        # n = len(nums)
        # dp = [-1] * n

        # def rob(i):
        #     if i == 0:
        #         return nums[i]
        #     if i < 0:
        #         return 0
            
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     pick = nums[i] + rob(i - 2)
        #     not_pick = rob(i - 1)

        #     dp[i] = max(pick, not_pick)

        #     return dp[i]
    
        # return rob(n - 1)

        # 2. tabulation bottom-up

        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]

        for i in range(1, n):
            take = nums[i] + dp[i - 2] if i > 1 else nums[i]
            not_take = dp[i - 1]

            dp[i] = max(take, not_take)
        
        return dp[n - 1]