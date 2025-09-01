class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            freqs = {}
            count = 0
            l = r = 0

            while r < len(nums):
                freqs[nums[r]] = freqs.get(nums[r], 0) + 1

                while len(freqs) > k:
                    freqs[nums[l]] -= 1
                    if freqs[nums[l]] == 0:
                        del freqs[nums[l]]
                    l += 1
                
                count += r - l + 1
                r += 1
            
            return count
        
        return atMost(k) - atMost(k - 1)