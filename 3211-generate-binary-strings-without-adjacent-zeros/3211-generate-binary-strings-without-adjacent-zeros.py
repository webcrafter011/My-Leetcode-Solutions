class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def build(st=''):
            if len(st) == n:
                ans.append(st)
                return 
            
            build(st + '1')

            if not st or st[-1] == '1':
                build(st + '0')
            
        build()
        return ans