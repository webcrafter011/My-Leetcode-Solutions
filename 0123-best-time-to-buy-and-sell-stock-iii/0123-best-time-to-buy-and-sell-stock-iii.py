class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # def solve(i, buy, transactions):
        #     if transactions >= 2 or i == n:
        #         return 0
            
        #     if dp[i][buy][transactions] != -1:
        #         return dp[i][buy][transactions]

        #     profit = 0
        #     if buy:
        #         profit = max(
        #             -prices[i] + solve(i + 1, 0, transactions),
        #             solve(i + 1, 1, transactions)
        #         )
        #     else:
        #         profit = max(
        #             prices[i] + solve(i + 1, 1, transactions + 1),
        #             solve(i + 1, 0, transactions)
        #         )
            
        #     dp[i][buy][transactions] = profit
        #     return profit
        
        # return solve(0, 1, 0)

        # Tabulation solution 
        dp = [[0] * 3 for _ in range(2)]

        for i in range(n - 1, -1, -1):
            curr = [[0] * 3 for _ in range(2)]
            for buy in range(2):
                for transactions in range(2):
                    profit = 0
                    if buy:
                        profit = max(
                            -prices[i] + dp[0][transactions],
                            dp[1][transactions]
                        )
                    else:
                        profit = max(
                            prices[i] + dp[1][transactions + 1],
                            dp[0][transactions]
                        )
                    
                    curr[buy][transactions] = profit
            dp = curr
        
        return dp[1][0]