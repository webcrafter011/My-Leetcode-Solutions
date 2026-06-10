class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        rem = [0] * len(s)
        op = 0

        # mark the string that are supposed to be taken out 
        for i, c in enumerate(s):
            if c == '(':
                if op == 0:
                    rem[i] = -1
                op += 1
            elif c == ')':
                op -= 1
                if op == 0:
                    rem[i] = -1
        
        ans = ''
        for i in range(len(s)):
            if rem[i] != -1:
                ans += s[i]
        
        return ans