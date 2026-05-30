class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        suffix, prefix = 1, 1
        n = len(nums)

        for i in range(n):
            if suffix == 0: suffix = 1
            if prefix == 0: prefix = 1

            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            ans = max(ans, max(prefix, suffix))
        
        return ans
