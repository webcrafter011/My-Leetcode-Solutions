class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(set(arr))
        h = {}

        for i, num in enumerate(sortedArr):
            h[num] = i + 1
        
        return [h[num] for num in arr]
