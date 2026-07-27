class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # maxi = float('-inf')

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         maxi = max(maxi, (nums[i] - 1) * (nums[j] - 1))
        
        # return maxi
        
        # Approach 2 sort
        # maxi = float('-inf')
        # nums.sort()

        # return (nums[-1] - 1) * (nums[-2] - 1)

        # Approach 3: track 2 largest numbers of the array 

        m1 = m2 = float('-inf')

        for i in range(n):
            if m1 < nums[i]:
                m2 = m1
                m1 = nums[i]
            elif m2 < nums[i]:
                m2 = nums[i]

        print(f"m1 = {m1}, m2 = {m2}")
        return (m1 - 1) * (m2 - 1)