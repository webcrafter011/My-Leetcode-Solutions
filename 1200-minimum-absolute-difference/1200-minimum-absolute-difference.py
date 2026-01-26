class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        pairs = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                pairs = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                pairs.append([arr[i - 1], arr[i]])
        
        return pairs
