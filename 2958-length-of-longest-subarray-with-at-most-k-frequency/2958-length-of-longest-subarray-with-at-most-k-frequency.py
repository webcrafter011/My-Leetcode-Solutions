class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxi = float('-inf')
        i = j = 0
        n = len(nums)
        freq = {}

        while i < n and j < n:
            freq[nums[j]] = freq.get(nums[j], 0) + 1

            while i < n and freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1
            
            maxi = max(maxi, j - i + 1)
            
            j += 1
        
        return maxi