class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        j = 0
        maxFreq = 0
        counts = {}
        res = 0

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            maxFreq = max(maxFreq, counts[s[i]])

            while (i - j + 1) - maxFreq > k:
                # maxFreq = 0
                counts[s[j]] -= 1
                j += 1
            
            res = max(res, i - j + 1)
        
        return res