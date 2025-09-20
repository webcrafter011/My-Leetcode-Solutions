class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def getMax(k):
            count = left = 0
            freqs = {}

            for right in range(len(nums)):
                freqs[nums[right]] = freqs.get(nums[right], 0) + 1

                while len(freqs) > k:
                    freqs[nums[left]] -= 1
                    if freqs[nums[left]] == 0:
                        del freqs[nums[left]]
                    left += 1
                
                count += right - left + 1

            return count
                        
        return getMax(k) - getMax(k - 1)