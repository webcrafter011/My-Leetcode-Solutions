class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_max(arr):
            arr.sort()
            maxi = 0
            count = 0
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    count += 1
                    maxi = max(count, maxi)
                else:
                    count = 0
            
            return maxi + 2
        
        max_v = get_max(vBars)
        max_h = get_max(hBars)
        return min(max_v, max_h) ** 2