class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def dig_sum(num):
            num = str(num)
            return sum([int(n) for n in num])
            

        for i in range(len(nums)):
            if i == dig_sum(nums[i]):
                return i
        
        return -1