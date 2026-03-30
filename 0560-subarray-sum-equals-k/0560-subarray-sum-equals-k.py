class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        # key -> curr_sum, value -> frequency 
        pre_sum = {0:1}

        count = 0
        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum - k in pre_sum:
                count += pre_sum[curr_sum - k]
            
            pre_sum[curr_sum] = pre_sum.get(curr_sum, 0) + 1
        
        return count