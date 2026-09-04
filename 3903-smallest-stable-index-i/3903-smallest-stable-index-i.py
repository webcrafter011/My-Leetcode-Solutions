class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = [-1] * n
        mini = [float('-inf')] * n
        maxi[0] = nums[0]
        mini[n - 1] = nums[n - 1]

        for i in range(1, n):
            maxi[i] = max(maxi[i - 1], nums[i])
        
        for i in range(n - 2, -1, -1):
            mini[i] = min(nums[i], mini[i + 1])
        
        for i in range(n):
            res = maxi[i] - mini[i]
            print(f"for i = {i} maxi[i] = {maxi[i]} and mini[i] = {mini[i]}")
            if res <= k:
                return i
            
        return -1