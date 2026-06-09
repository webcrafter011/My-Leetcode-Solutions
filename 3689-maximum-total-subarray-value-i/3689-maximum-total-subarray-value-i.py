class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxi = max(nums)
        mini = min(nums)

        return (maxi - mini) * k