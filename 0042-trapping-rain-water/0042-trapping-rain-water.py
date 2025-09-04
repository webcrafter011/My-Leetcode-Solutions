class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        suf_max = [None] * n
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])
        
        left_max = float('-inf')
        trapped_water = 0
        for i in range(n):
            left_max = max(left_max, height[i])
            right_max = suf_max[i]
            if height[i] < left_max and height[i] < right_max:
                trapped_water += min(left_max, right_max) - height[i]
            
        
        return trapped_water