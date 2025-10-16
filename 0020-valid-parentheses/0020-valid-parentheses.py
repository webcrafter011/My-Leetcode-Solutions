class Solution:
    def isValid(self, s: str) -> bool:
        openings = {')': '(', '}': '{', ']': '['}
        st = []

        for char in s:
            if char in openings.values():
                st.append(char)
            elif not st or openings[char] != st.pop():
                return False
        
        return not st
        
