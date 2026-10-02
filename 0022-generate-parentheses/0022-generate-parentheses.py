class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def build(s = '', op = 0, cnt = 0):
            if len(s) == 2 * n:
                if cnt == n:
                    res.append(s)
                return
            
            if op < n:
                build(s + '(', op + 1, cnt)

            if op:
                build(s + ')', op - 1, cnt + 1)
        
        build()

        return res
