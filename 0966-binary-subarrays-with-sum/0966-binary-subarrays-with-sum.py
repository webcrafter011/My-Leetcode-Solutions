class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def getMax(goal):
            if goal < 0:
                return 0

            left = count = currSum = 0

            for right in range(len(nums)):
                currSum += nums[right]

                while currSum > goal:
                    currSum -= nums[left]
                    left += 1
                
                count += (right - left + 1)
            
            return count
        
        return getMax(goal) - getMax(goal - 1)

