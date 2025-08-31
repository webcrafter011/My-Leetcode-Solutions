class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        h = {'a': 0, 'b': 0, 'c': 0}
        r = l = 0
        count = 0

        while r < len(s):
            h[s[r]] = h.get(s[r], 0) + 1

            while h['a'] > 0 and h['b'] > 0 and h['c'] > 0:
                h[s[l]] -= 1
                count += len(s) - r
                l += 1

            r += 1
        
        return count