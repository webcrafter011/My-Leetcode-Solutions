class Solution:
    def numberOfSubstrings(self, s: str) -> int:  
        h = {
            'a': 0,
            'b': 0,
            'c': 0
        }
        left = count = 0

        for right in range(len(s)):
            h[s[right]] = h.get(s[right], 0) + 1

            while h['a'] > 0 and h['b'] > 0 and h['c'] > 0:
                count += len(s) - right
                h[s[left]] -= 1
                left += 1
            
        return count