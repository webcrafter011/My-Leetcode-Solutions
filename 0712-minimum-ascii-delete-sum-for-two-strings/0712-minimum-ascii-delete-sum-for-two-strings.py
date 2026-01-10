class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def find_ascii_value(s):
            total = 0
            for char in s:
                total += ord(char)
            return total

        total = find_ascii_value(s1) + find_ascii_value(s2)
        n, m = len(s1), len(s2)
        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # def solve(i, j):
        #     if i < 0 or j < 0:
        #         return 0
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if s1[i] == s2[j]:
        #         return ord(s1[i]) + solve(i - 1, j - 1)
            
        #     dp[i][j] = max(solve(i - 1, j), solve(i, j - 1))
        #     return dp[i][j] 
        
        # return total - 2 * solve(n - 1, m - 1)

        # Tabulation Approach

        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         if s1[i - 1] == s2[j - 1]:
        #             dp[i][j] = ord(s1[i - 1]) + dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # return total - 2 * dp[n][m]

        # Space Optimization
        dp = [0] * (m + 1) 

        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = ord(s1[i - 1]) + dp[j - 1]
                else:
                    curr[j] = max(dp[j], curr[j - 1])
            dp = curr

        return total - 2 * dp[m]

