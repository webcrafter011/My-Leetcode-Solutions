class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def dig_sum(num):
            return sum([int(n) for n in num])

        while len(s) > k:
            new = ''

            for i in range(0, len(s), k):
                # print(dig_sum(s[i:(i + k)]))
                c = str(dig_sum(s[i:(i + k)]))
                
                new += c
            
            s = new
        
        return s
