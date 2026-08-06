class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def dig_prod(d):
            return math.prod(list(map(int, str(d))))
        

        while True:
            total = dig_prod(n)
            if total % t == 0:
                return n
            n += 1
        
