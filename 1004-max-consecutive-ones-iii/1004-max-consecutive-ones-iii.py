class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        maxi = 0
        n = len(nums)
        zero = 0

        for i in range(n):
            if nums[i] == 0:
                zero += 1
            
            while zero > k:
                if nums[j] == 0:
                    zero -= 1
                j += 1
                    
            current = i - j + 1
            maxi = max(maxi, current)
        
        return maxi