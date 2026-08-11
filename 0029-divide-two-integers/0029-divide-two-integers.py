class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        sign = True
        if dividend >= 0 and divisor < 0: sign = False
        if dividend < 0 and divisor > 0: sign = False

        n = abs(dividend)
        d = abs(divisor)

        while n >= d:
            count = 0
            while n >= (d << (count + 1)):
                count += 1
            ans += 1 << count
            n = n - (d << count)
        
        if ans == (1 << 31) and sign:
            return 2**31 - 1
        
        if ans == (1 << 31) and not sign:
            return -2**31
        
        if sign:
            return ans
        else:
            return -ans
            