class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        arr2.sort()

        for x in arr1:
            l, r = 0, len(arr2)

            while l < r:
                mid = (l + r) // 2
                
                if arr2[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            
            ok = True
        
            if l < len(arr2) and abs(arr2[l] - x)  <= d:
                ok = False
            elif l > 0 and abs(arr2[l - 1] - x) <= d:
                ok = False
            if ok:
                count += 1
        
        return count