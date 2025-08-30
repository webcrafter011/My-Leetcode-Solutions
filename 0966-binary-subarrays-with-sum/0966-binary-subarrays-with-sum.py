class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # sum_map = {0:1}
        # pre_sum = 0
        # count = 0

        # for num in nums:
        #     pre_sum += num

        #     if pre_sum - goal in sum_map:
        #         count += sum_map[pre_sum - goal]
            
        #     sum_map[pre_sum] = sum_map.get(pre_sum, 0) + 1
        
        # return count

        def atMax(k):
            l = 0
            r = 0
            count = 0
            curr_sum = 0

            while r < len(nums):
                curr_sum += nums[r]

                while curr_sum > k and l <= r:
                    curr_sum -= nums[l]
                    l += 1
                
                count += r - l + 1
                r += 1
                
            return count

        return atMax(goal) - atMax(goal - 1)