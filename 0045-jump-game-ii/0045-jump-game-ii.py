class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = r = l = 0
        n = len(nums)

        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest 
            jumps += 1
        return jumps