class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n   
        rightSum = [0] * n
        left = 0
        right = 0

        for i in range(n):
            left += nums[i]
            leftSum[i] = left

        for i in range(n-1, -1, -1):
            right += nums[i]
            rightSum[i] = right
        

        ans = []

        for i in range(n):
            ans.append(abs(leftSum[i] - rightSum[i]))
        
        return ans