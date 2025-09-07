class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        maxLen = 0
        j = 0
        for i in range(len(s)):
            while s[i] in h:
                del h[s[j]]
                j += 1
            
            h[s[i]] = True
            maxLen = max(maxLen, i - j + 1)
        
        return maxLen