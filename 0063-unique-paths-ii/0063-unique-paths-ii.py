class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]

        # def solve(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if obstacleGrid[i][j] == 1:
        #         return 0
        #     if i == 0 and j == 0:
        #         return 1
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     up = solve(i - 1, j)
        #     left = solve(i, j - 1)
            
        #     dp[i][j] = up + left
        #     return up + left
        
        # return solve(m - 1, n - 1)

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = left = 0
                    if i > 0:
                        up = dp[i - 1][j]
                    if j > 0:
                        left = dp[i][j - 1]
                    dp[i][j] = up + left
        
        return dp[m - 1][n - 1]
                    