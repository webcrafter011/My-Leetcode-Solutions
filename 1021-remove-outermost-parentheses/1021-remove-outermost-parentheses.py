class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []    
        count = 0

        for c in s:
            if c == '(':
                if count == 0:
                    count += 1
                    continue
                count += 1
            else:
                if count == 1:
                    count -= 1
                    continue
                count -= 1

            res.append(c)
        
        return ''.join(res)