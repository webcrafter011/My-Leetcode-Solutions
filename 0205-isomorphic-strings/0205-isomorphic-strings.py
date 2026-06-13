class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] in s_map and t[i] != s_map[s[i]]:
                return False
            if t[i] in t_map and s[i] != t_map[t[i]]:
                return False
            
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]

        return True