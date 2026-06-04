class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2

            missing_count = nums[mid] - (mid + 1)
            if missing_count >= k:
                high = mid 
            else:
                low = mid + 1
        
        return low + k