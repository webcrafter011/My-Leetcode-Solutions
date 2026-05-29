class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def get_digits_square_sum(num):
            total = 0

            while num > 0:
                total += (num % 10) ** 2
                num //= 10
            
            return total
        

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_digits_square_sum(n)
        
        if n == 1:
            return True
        return False