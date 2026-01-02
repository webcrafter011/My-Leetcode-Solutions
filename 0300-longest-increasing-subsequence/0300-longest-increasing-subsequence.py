class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n  = len(nums)
        dp = [1] * (n + 1)

        # for i in range(n - 1, -1, -1):
        #     curr = [0] * (n + 1)
        #     for prev in range(i - 1, -2, -1):
        #         not_take = dp[prev + 1]
        #         take = 0
        #         if prev == -1 or nums[prev] < nums[i]:
        #             take = 1 + dp[i + 1]
                
        #         curr[prev + 1] = max(not_take, take)
        #     dp = curr
        # return dp[0]

        for i in range(n):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    dp[i] = max(dp[i], dp[prev] + 1)
        
        return max(dp)