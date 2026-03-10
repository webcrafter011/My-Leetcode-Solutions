class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            sorted = True
            for j in range(i, i + n - 1):
                if nums[j % n] > nums[(j + 1) % n]:
                    sorted = False
                    break
            if sorted:
                return True
        
        return False
                                    