class Solution:
    def canAliceWin(self, n: int) -> bool:
        p = 0 # player 0 is alice and 1 is bob 
        r = 10

        while True:
            if n < r:
                if p == 1:
                    return True
                else:
                    return False
            
            p ^= 1
            n -= r
            r -= 1
            if r < 0:
                return False
        
        