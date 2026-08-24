class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [None] * n # left max
        suf_max = [None] * n # right max
        pre_max[0] = height[0]
        suf_max[n - 1] = height[n - 1]

        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])
        
        water = 0
        for i in range(n):
            if height[i] < pre_max[i] and height[i] < suf_max[i]:
                water += min(pre_max[i], suf_max[i]) - height[i]
        
        return water