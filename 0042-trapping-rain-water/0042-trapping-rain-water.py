class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = rmax = water = 0
        l, r = 0, n - 1

        while l < r:
            if height[l] < height[r]:
                if lmax > height[l]:
                    water += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if rmax > height[r]:
                    water += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
            
        return water