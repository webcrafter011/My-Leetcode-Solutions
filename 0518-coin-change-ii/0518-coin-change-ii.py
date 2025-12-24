from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        
        def solve(i, target):
            if i == 0:
                if target % coins[0] == 0:
                    return 1
                return 0
            
            if dp[i][target] != -1:
                return dp[i][target]

            not_take = solve(i - 1, target)
            take = 0
            if coins[i] <= target:
                take = solve(i, target - coins[i])
            
            dp[i][target] = take + not_take
            return dp[i][target]
        

        return solve(n - 1, amount)

            