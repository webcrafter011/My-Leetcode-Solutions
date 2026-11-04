class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = nums[::]

        for num in nums:
            res.append(num)
        
        return res