class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [0] * n

        less = 0
        greator = n - 1

        for i, j in zip(range(n), range(n - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less] = nums[i]
                less += 1
            if nums[j] > pivot:
                ans[greator] = nums[j]
                greator -= 1
        
        while less <= greator:
            ans[less] = pivot
            less += 1
    
        return ans