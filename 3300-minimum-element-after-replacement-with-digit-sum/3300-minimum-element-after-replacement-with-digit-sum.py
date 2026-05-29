class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = float('inf')

        def get_digits_sum(num):
            return sum(list(map(int, str(num))))

        for num in nums:
            mini = min(mini, get_digits_sum(num))
        
        return mini