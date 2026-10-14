class Solution:
    def maxSumOfSquares(self, num: int, summation: int) -> str:
        total = summation
        res = ''
        curr = 9

        while total or len(res) < num:
            if total < curr:
                curr -= 1
                continue
            
            total -= curr
            res += str(curr)
        
        return res if len(res) == num else ''