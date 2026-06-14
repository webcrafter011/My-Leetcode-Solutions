class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        op = 0

        for c in s:
            if c == '(':
                op += 1
                maxi =  max(maxi, op)
            elif c == ')':
                op -= 1
        
        return maxi