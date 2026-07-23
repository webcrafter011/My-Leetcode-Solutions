class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn = abs(n)
        ans = 1
        
        while nn:
            # for odd power
            if nn & 1:
                ans *= x
                nn -= 1
            else:
                nn //= 2
                x *= x
        
        if n < 0:
            return 1/ans
        return ans