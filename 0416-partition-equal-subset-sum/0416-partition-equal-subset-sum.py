class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        n = len(nums)
        if summation % 2 == 0:
            summation //= 2
        else:
            return False

        dp = [[False] * (summation + 1) for _ in range(n)]

        # def solve(i, k):
        #     if k == 0:
        #         return True
        #     if i == 0:
        #         return nums[0] == k
            
        #     if dp[i][k] != -1:
        #         dp[i][k] = True

        #     not_take = solve(i - 1, k)
        #     take = False
        #     if nums[i] <= k:
        #         take = solve(i - 1, k - nums[i])
            
        #     dp[i][k] = take or not_take
        #     return dp[i][k]
        
        for i in range(n):
            dp[i][0] = True
        
        if nums[0] <= summation:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for target in range(1, summation + 1):
                not_take = dp[i - 1][target]

                take = False
                if nums[i] <= target:
                    take = dp[i - 1][target - nums[i]]
                
                dp[i][target] = take or not_take


        return dp[n - 1][summation]