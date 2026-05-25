class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        trips = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            l, r = i + 1, n - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    trips.append([nums[i], nums[l], nums[r]])

                    r -= 1

                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
        
        return trips