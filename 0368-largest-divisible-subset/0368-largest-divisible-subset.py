class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = list(range(n))

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    parent[i] = j
        
        max_len = max(dp)
        idx = dp.index(max_len)

        lds = []
        while parent[idx] != idx:
            lds.append(nums[idx])
            idx = parent[idx]

        lds.append(nums[idx])
        return lds[::-1]