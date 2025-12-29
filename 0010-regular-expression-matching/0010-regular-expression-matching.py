class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        

        def solve(i, j):
            # base cases
            if i < 0 and j < 0:
                return True
            
            if j < 0:
                return False
            
            if i < 0:
                while j >= 0:
                    if p[j] == '*':
                        j -= 2
                    else:
                        return False
                return True
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == p[j] or p[j] == '.':
                dp[i][j] = solve(i - 1, j - 1)
            elif p[j] == '*':
                skip = solve(i, j - 2)
                consume = False
                if s[i] == p[j - 1] or p[j - 1] == '.':
                    consume = solve(i - 1, j)

                dp[i][j] = skip or consume
            else:
                dp[i][j] = False
            
            return dp[i][j]
        
        return solve(n - 1, m - 1)