class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def get_most(goal):
            if goal <= 0:
                return 0

            count = 0
            left = 0
            h = {}

            for right in range(len(nums)):
                h[nums[right]] = h.get(nums[right], 0) + 1

                while len(h) > goal:
                    h[nums[left]] -= 1
                    if h[nums[left]] == 0:
                        del h[nums[left]]
                    left += 1
                
                
                count += (right - left + 1)
            
            return count
        
        return get_most(k) - get_most(k - 1)