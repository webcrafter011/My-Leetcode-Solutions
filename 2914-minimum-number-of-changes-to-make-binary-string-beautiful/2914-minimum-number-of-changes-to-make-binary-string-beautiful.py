class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            if i % 2 != 0 and s[i] != s[i - 1]:
                res += 1

        return res
