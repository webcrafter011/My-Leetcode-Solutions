from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sqr = n * n
        return gcd(sqr, sqr + n)