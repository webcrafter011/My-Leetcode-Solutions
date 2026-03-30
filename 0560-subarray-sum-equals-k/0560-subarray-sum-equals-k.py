class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        pre_sum = {0:-1}
        count = 0
        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum - k in pre_sum:
                count += 1
            
            if curr_sum not in pre_sum:
                pre_sum[curr_sum] = i
        
        return count