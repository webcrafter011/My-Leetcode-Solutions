class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n)]

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

            # not_take = solve(i - 1, target)
            # take = float('inf')
            # if coins[i] <= target:
            #     take = 1 + solve(i, target - coins[i])
            # dp[i][target] = min(take, not_take)
        #     return dp[i][target]

        # Tabulation:

        for target in range(amount + 1):
            if target % coins[0] == 0:
                dp[0][target] = target // coins[0]
            
        for i in range(1, n):
            for target in range(amount + 1):
                not_take = dp[i - 1][target]
                take = float('inf')
                if coins[i] <= target:
                    take = 1 + dp[i][target - coins[i]]
                dp[i][target] = min(take, not_take)


            
        ans = dp[n - 1][amount]
        return ans if ans != float('inf') else -1