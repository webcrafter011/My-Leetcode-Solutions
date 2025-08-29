class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        i = j = 0
        maxLen = 0
        while i <= j and j < len(s):
            while s[j] in h:
                del h[s[i]]
                i += 1
            h[s[j]] = True
            maxLen = max(maxLen, (j - i + 1))
            j += 1
    
        return maxLen