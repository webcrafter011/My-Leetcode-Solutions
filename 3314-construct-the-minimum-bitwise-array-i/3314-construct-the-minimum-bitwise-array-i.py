class Solution:
    def minBitwiseArray(self, nums):
        res = []
        for p in nums:
            if p == 2:           
                res.append(-1)
                continue
            m = p + 1
            k = 0
            while m % 2 == 0:
                m //= 2
                k += 1
            ans = p - (1 << (k - 1))
            res.append(ans)
        return res
