from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        i = 0
        while i < len(nums):
            if counts[0] != 0:
                nums[i] = 0
                counts[0] -= 1
            elif counts[1] != 0:
                nums[i] = 1
                counts[1] -= 1
            elif counts[2] != 0:
                nums[i] = 2
                counts[2] -= 1
            i += 1