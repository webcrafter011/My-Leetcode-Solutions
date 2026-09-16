class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        
        def get_at_most(target):
            # this function returns the number of subarrays that sum up to at most target

            if target < 0:
                return 0

            res = 0
            left = 0
            count = 0

            for right in range(len(nums)):
                count += nums[right]

                while count > target:
                    count -= nums[left]
                    left += 1
                
                res += right - left + 1
            
            return res
        

        # we will return the number of subarrays that sum up to target - number of subarrays that sum up to (target - 1) in result we end up with the exact number of subarray that sum up to exactly target
        
        return get_at_most(goal) - get_at_most(goal - 1)