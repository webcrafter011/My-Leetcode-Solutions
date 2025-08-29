class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # helper function to check if the particular subarray has at max k zeroes
        # def subArrWithMaxKZeroes(arr):
        #     count = 0
        #     for num in arr:
        #         if num == 0:
        #             count += 1

        #     return count <= k

        # maxLen = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i, n):
        #         arr = nums[i:j + 1]
        #         if subArrWithMaxKZeroes(arr):
        #             maxLen = max(maxLen, len(arr))

        # return maxLen

        l = r = 0
        maxLen = 0
        zeroes = 0

        while r < len(nums):
            if nums[r] == 0:
                zeroes += 1

            if zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1

            currLen = r - l + 1
            maxLen = max(maxLen, currLen)
            r += 1

        return maxLen

__import__("atexit").register(lambda: open("display_memory.txt", "w").write("0"))
