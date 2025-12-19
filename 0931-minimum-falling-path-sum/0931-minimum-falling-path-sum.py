class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[-1] * n for _ in range(n)]

        # def topdown(i, j):
        #     if j < 0 or j > n - 1:
        #         return float('inf')

        #     if i == n - 1:
        #         return matrix[i][j]
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     down = matrix[i][j] + topdown(i + 1, j)
        #     left = matrix[i][j] + topdown(i + 1, j - 1)
        #     right = matrix[i][j] + topdown(i + 1, j + 1)

        #     dp[i][j] = min([down, left, right])
        #     return dp[i][j]
        
        # return min([topdown(0, i) for i in range(n)])

        # 2. Tabulation
        for i in range(n):
            dp[n - 1][i] = matrix[n - 1][i]
        
        for i in range(n - 2, -1, -1):
            for j in range(n):
                down = left = right = float('inf')

                down = matrix[i][j] + dp[i + 1][j]

                
                if j - 1 >= 0:
                    left = matrix[i][j] + dp[i + 1][j - 1]
                
                if j + 1 <= n - 1:
                    right = matrix[i][j] + dp[i + 1][j + 1]
                
                dp[i][j] = min([down, left, right])
        
        return min([dp[0][i] for i in range(n)])