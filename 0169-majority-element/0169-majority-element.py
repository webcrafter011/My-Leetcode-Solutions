class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        el = None

        for i in range(len(nums)):
            if count == 0:
                el = nums[i]
                count += 1
            elif el == nums[i]:
                count += 1
            else:
                count -= 1
        
        return el