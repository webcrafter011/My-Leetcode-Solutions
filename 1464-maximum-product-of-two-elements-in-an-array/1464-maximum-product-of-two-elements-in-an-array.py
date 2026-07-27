class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float('-inf')

        for i in range(n):
            for j in range(i + 1, n):
                maxi = max(maxi, (nums[i] - 1) * (nums[j] - 1))
        
        return maxi