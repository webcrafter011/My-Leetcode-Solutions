class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxi = float('-inf')
        n = len(colors)
        houses = {}

        for i in range(n):
            if colors[i] not in houses:
                for j in range(n):
                    if colors[j] != colors[i]:
                        maxi = max(maxi, abs(i - j))
                houses[colors[i]] = True
        
        return maxi