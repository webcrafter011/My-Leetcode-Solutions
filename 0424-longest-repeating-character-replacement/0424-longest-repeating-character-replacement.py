class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        res = 0
        maxFreq = 0
        left = 0


        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freqs[s[right]])

            while right - left + 1 > maxFreq + k:
                freqs[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res