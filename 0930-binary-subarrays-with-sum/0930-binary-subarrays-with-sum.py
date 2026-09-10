class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(target):
            count = 0
            left = 0
            res = 0

            for right in range(len(nums)):
                if target < 0:
                    return 0
                    
                count += nums[right]

                while count > target:
                    count -= nums[left]
                    left += 1
                
                res += (right - left + 1)
            
            return res
        
        return at_most(goal) - at_most(goal - 1)