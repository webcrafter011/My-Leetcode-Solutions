class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = float('-inf')
        curr_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
                max_count = max(max_count, curr_count)
            else:
                curr_count = 0
        
        return max_count if max_count != float('-inf') else 0