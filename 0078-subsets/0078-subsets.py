class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def recurse(i, sub): 
            if i == n:
                res.append(sub[::])
                return
            
            sub.append(nums[i])
            recurse(i + 1, sub)
            sub.pop()
            recurse(i + 1, sub)
        
        recurse(0, [])
        return res