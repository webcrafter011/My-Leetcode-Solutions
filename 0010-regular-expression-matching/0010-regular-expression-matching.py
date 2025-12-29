class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        

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


            if s[i] == p[j] or p[j] == '.':
                return solve(i - 1, j - 1)
            elif p[j] == '*':
                skip = solve(i, j - 2)
                consume = False
                if s[i] == p[j - 1] or p[j - 1] == '.':
                    consume = solve(i - 1, j)

                return skip or consume
            else:
                return False
        
        return solve(n - 1, m - 1)