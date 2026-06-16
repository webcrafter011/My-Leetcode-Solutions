class Solution:
    def processStr(self, s: str) -> str:
        res = ''

        for c in s:
            if c.isalpha():
                res += c
            elif c == '*':
                if len(res) > 0:
                    res = res[:-1]
            elif c == '#':
                res += res
            elif c == '%':
                res = res[::-1]
        
        return res