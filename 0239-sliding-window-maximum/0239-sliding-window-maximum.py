from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi = []
        # for i in range(len(nums) - k + 1):
        #     maxi.append(max(nums[i:k+i]))
        
        # return maxi

        # Optimal approach using dq (monotonic stack)
        dq = deque()
        for i in range(len(nums)):
            # pop the elements outside the k length window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # pop the smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                maxi.append(nums[dq[0]])
        
        return maxi