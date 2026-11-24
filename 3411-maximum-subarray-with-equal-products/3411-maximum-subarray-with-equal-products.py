import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        maxi = 0

        def calc(arr):
            lcm = prod = gcd = arr[0]

            for i in range(1, len(arr)):
                prod *= arr[i]
                lcm = math.lcm(lcm, arr[i])
                gcd = math.gcd(gcd, arr[i])
            
            return len(arr) if prod == (gcd * lcm) else 0
        

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                maxi = max(maxi, calc(nums[i:j + 1]))
        
        return maxi