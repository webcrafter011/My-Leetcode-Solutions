class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient  = 0
 
        neg = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            shift = 0

            while dividend >= (divisor << (shift + 1)):
                shift += 1
            
            quotient += 1 << shift
            dividend -= divisor << shift
        
        if quotient == 2 ** 31 and neg:
            return -2 ** 31
        elif quotient == 2 ** 31 and not neg:
            return 2 ** 31 - 1
        
        if neg:
            return -quotient
        else:
            return quotient