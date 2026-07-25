class Solution:
    def maxProduct(self, n: int) -> int:
        nums = list(map(int, str(n)))

        nums.sort()


        return nums[-1] * nums[-2]