class Solution:
    def myPow(self, x: float, n: int) -> float:
        # nn = abs(n)
        # ans = 1
        
        # while nn:
        #     # for odd power
        #     if nn & 1:
        #         ans *= x
        #         nn -= 1
        #     else:
        #         nn //= 2
        #         x *= x
        
        # if n < 0:
        #     return 1/ans
        # return ans
        

        def calc(base: float, power: int, ans: float):
            if power == 0:
                return ans
            
            # odd power
            if power & 1:
                return calc(base, power - 1, ans * base)
            
            return calc(base * base, power // 2, ans)

        ans = calc(x, abs(n), 1)
        if n < 0:
            return 1/ans
        return ans