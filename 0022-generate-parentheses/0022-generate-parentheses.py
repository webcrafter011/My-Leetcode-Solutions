class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def build(st='(', op=1, cl=0):
            if op > n:
                return 
            if op == n and op == cl:
                res.append(st)
                return
            
            if op != cl:
                build(st + ')', op, cl + 1)
            
            build(st + '(', op + 1, cl)
            
            

        build()

        return res
        