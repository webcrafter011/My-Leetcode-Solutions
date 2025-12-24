from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # def solve(i, target):
        #     if target == 0:
        #         return 0 

        #     if i == 0:
        #         if target % coins[i] == 0:
        #             return target // coins[i]
        #         else:
        #             return float('inf')
            
        #     if dp[i][target] != -1:
        #         return dp[i][target]

        #     not_take = solve(i - 1, target)
        #     take = float('inf')
        #     if coins[i] <= target:
        #         take = 1 + solve(i, target - coins[i])
        #     dp[i][target] = min(take, not_take)
        #     return dp[i][target]

        # Tabulation: Optimized
        # dp = [float('inf')] * (amount + 1)
        
        # for target in range(amount + 1):
        #     if target % coins[0] == 0:
        #         dp[target] = target // coins[0]

        # for i in range(1, n):
        #     curr = [float('inf')] * (amount + 1)
        #     for target in range(amount + 1):
        #         not_take = dp[target]
        #         take = float('inf')
        #         if coins[i] <= target:
        #             take = 1 + curr[target - coins[i]]
        #         curr[target] = min(take, not_take)

        #     dp = curr[::]

        # ans = dp[amount]

        @cache
        def solve(i, target):
            if target == 0:
                return 0
            
            if i == 0:
                if target % coins[0] == 0:
                    return target // coins[0]
                else:
                    return float('inf')
            
            
            not_take = solve(i - 1, target)

            take = float('inf')
            if coins[i] <= target:
                take = 1 + solve(i, target - coins[i])
            
            return min(take, not_take)

        ans = solve(n - 1, amount)

        return ans if ans != float('inf') else -1