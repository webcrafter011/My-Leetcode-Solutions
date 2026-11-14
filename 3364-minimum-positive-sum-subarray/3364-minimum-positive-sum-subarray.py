class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini = float('inf')
        pre_sum = {-1: 0}
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            pre_sum[i] = curr_sum

            if i >= l - 1:
                for j in range(max(-1, i - r), i - l + 1):
                    if (pre_sum[i] - pre_sum[j]) > 0:
                        mini = min(mini, pre_sum[i] - pre_sum[j])

        
        return mini if mini != float('inf') else - 1