class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def build(i=0, arr=[]):
            if i == n:
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            build(i + 1, arr)
            arr.pop()
            build(i + 1, arr)
        
        build()
        return res