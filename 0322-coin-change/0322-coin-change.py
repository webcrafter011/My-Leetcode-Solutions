class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        def solve(total):
            if total > amount:
                return float('inf')
            if total == amount:
                return 0
            if dp[total] != -1:
                return dp[total]
                
            mini = float('inf')
            for coin in coins:
                mini = min(mini, 1 + solve(total + coin))

            dp[total] = mini
            return mini

        ans = solve(0)
        return ans if ans != float('inf') else -1
