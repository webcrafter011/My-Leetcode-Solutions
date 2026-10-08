class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []    
        st = []

        for c in s:
            if c == '(':
                if not st:
                    st.append(c)
                    continue
                st.append(c)
            else:
                if len(st) == 1:
                    st.pop()
                    continue
                st.pop()

            res.append(c)
        
        return ''.join(res)