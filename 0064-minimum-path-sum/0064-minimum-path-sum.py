class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        # def topdown(i, j):
        #     if i == 0 and j == 0:
        #         return grid[i][j]
        #     if i < 0 or j < 0:
        #         return float('inf')
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     up = grid[i][j] + topdown(i - 1, j)
        #     left = grid[i][j] + topdown(i, j - 1)

        #     dp[i][j] = min(up, left)
        #     return dp[i][j]
        
        # return topdown(m - 1, n - 1)

        # statergy 2: tabulation

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    up = left = float('inf')
                    if i > 0:
                        up = grid[i][j] + dp[i - 1][j]
                    if j > 0:
                        left = grid[i][j] + dp[i][j - 1]
                    dp[i][j] = min(up, left)
            
        return dp[m - 1][n - 1]