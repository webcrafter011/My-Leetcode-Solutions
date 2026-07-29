class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def build(i = 0, arr = []):
            if i == n:
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            build(i + 1, arr)
            arr.pop()

            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            
            build(j, arr)
        
        build()
        return res