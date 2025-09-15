class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxFreq = maxLen = 0
        freqs = {}

        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freqs[s[right]])

            if (right - left + 1) - maxFreq > k:
                freqs[s[left]] -= 1
                maxFreq = 0
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen