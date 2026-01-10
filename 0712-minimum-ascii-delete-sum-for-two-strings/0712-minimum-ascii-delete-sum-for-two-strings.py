class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def find_ascii_value(s):
            total = 0
            for char in s:
                total += ord(char)
            return total

        total = find_ascii_value(s1) + find_ascii_value(s2)
        n, m = len(s1), len(s2)
        dp = [[-1] * m for _ in range(n)]
        
        def solve(i, j):
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                return ord(s1[i]) + solve(i - 1, j - 1)
            
            dp[i][j] = max(solve(i - 1, j), solve(i, j - 1))
            return dp[i][j] 
        
        return total - 2 * solve(n - 1, m - 1)