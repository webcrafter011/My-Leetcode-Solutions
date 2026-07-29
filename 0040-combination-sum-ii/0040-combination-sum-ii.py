class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort(    )
        
        def build(i, total, arr):
            if total == target:
                res.append(arr.copy())
                return
            
            if i == n or total > target:
                return
            
            arr.append(candidates[i])
            build(i + 1, total + candidates[i], arr)
            arr.pop()

            j = i
            while j < n and candidates[j] == candidates[i]:
                j += 1
            # if j >= n:
            #     return

            build(j, total, arr)

            
        
        build(0, 0, [])
        return res