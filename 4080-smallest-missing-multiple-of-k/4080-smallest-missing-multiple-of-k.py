class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        num = 1
        while True:
            if k * num not in nums_set:
                return k * num
            num += 1
            