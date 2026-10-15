class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0

        def calc(arr):
            nums = set()

            for num in arr:
                nums.add(num)
            
            return len(nums)

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                unique_count = calc(nums[i:j + 1])
                res += (unique_count * unique_count)

        
        return res
