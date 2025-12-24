class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        def solve(i, target):
            if i == 0:
                if target % coins[0] == 0:
                    return 1
                return 0
            
            not_take = solve(i - 1, target)
            take = 0
            if coins[i] <= target:
                take = solve(i, target - coins[i])
            
            return take + not_take
        

        return solve(n - 1, amount)

            