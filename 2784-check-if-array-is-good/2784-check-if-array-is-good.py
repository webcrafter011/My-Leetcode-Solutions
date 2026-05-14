class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        expected = 1
        n = len(nums)

        for i in range(n):
            if i == n - 1 and expected - 1 == nums[i]:
                return True
            if nums[i] != expected:
                return False
            expected += 1
                
        return False