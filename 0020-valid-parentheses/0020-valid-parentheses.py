class Solution:
    def isValid(self, s: str) -> bool:
        para_map = {')': '(', '}': '{', ']': '['}
        st = []

        for char in s:
            if char in para_map.values():
                st.append(char)
            else:
                if not st or st.pop() != para_map[char]:
                    return False
        
        return not st
