class Solution:
    def separateSquares(self, squares):
        low = float('inf')
        high = float('-inf')
        
        for x, y, l in squares:
            low = min(low, y)
            high = max(high, y + l)
        
        def area_diff(H):
            above = 0.0
            below = 0.0
            
            for x, y, l in squares:
                top = y + l
                
                if H <= y:
                    above += l * l
                elif H >= top:
                    below += l * l
                else:
                    below += (H - y) * l
                    above += (top - H) * l
            
            return above - below
        
        for _ in range(60):
            mid = (low + high) / 2
            if area_diff(mid) > 0:
                low = mid
            else:
                high = mid
        
        return low
