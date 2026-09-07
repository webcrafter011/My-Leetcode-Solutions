class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        n = len(s)
        i = 0
        maxi = 0

        for j in range(n):
            h[s[j]] = h.get(s[j], 0) + 1

            while h[s[j]] > 1:
                h[s[i]] -= 1
                i += 1
            
            current = j - i + 1
            maxi = max(maxi, current)

        return maxi