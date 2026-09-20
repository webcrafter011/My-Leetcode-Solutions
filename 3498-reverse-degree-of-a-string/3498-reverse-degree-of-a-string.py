class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            c = s[i]
            print(f'index in reversed alphabet: {27 - (ord(c) - 96)}')
            print(f'index in string: {i}')
            print(f'product is {i * 27 - (ord(c) - 96)}')
            curr = (27 - (ord(c) - 96)) * (i + 1)
            res += curr
        
        return res