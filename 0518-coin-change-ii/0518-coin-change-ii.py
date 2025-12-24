from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        
        # Top-Down solution written by myself
        # def solve(i, target):
        #     if i == 0:
        #         if target % coins[0] == 0:
        #             return 1
        #         return 0
            
        #     if dp[i][target] != -1:
        #         return dp[i][target]

        #     not_take = solve(i - 1, target)
        #     take = 0
        #     if coins[i] <= target:
        #         take = solve(i, target - coins[i])
            
        #     dp[i][target] = take + not_take
        #     return dp[i][target]
        
        # Tabulation
        for target in range(amount + 1):
            if target % coins[0] == 0:
                dp[0][target] = 1
        
        for i in range(1, n):
            for target in range(amount + 1):
                not_take = dp[i - 1][target]
                take = 0
                if coins[i] <= target:
                    take = dp[i][target - coins[i]]
                
                dp[i][target] = take + not_take
                

        return dp[n - 1][amount]

            