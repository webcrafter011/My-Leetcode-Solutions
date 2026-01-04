class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        total = 0
        for n in nums:
            # case 1: p^3 = n and p is prime then sum of divisors is
            # 1 + p + p^2 + n
            p = round(n ** (1 / 3)) # taking cube root of n
            if p**3 == n and is_prime(p):
                total += (1 + p + p*p + n)
                continue
            
            # case2: n = p*q, p and q should be prime
            p = 2
            while p*p <= n:
                if n % p == 0:
                    q = n // p
                    if p!=q and is_prime(p) and is_prime(q):
                        total += (1 + p + q + n)
                        break
                p += 1
        
        return total