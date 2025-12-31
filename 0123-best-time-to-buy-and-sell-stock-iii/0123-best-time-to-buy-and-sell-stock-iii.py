class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]

        def solve(i, buy, transactions):
            if transactions >= 2 or i == n:
                return 0
            
            if dp[i][buy][transactions] != -1:
                return dp[i][buy][transactions]

            profit = 0
            if buy:
                profit = max(
                    -prices[i] + solve(i + 1, 0, transactions),
                    solve(i + 1, 1, transactions)
                )
            else:
                profit = max(
                    prices[i] + solve(i + 1, 1, transactions + 1),
                    solve(i + 1, 0, transactions)
                )
            
            dp[i][buy][transactions] = profit
            return profit
        
        return solve(0, 1, 0)