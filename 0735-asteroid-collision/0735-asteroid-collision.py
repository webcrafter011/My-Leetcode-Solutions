class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # time complexity: O(2n)
        # space complexity: O(n)
        st = []
        for ast in asteroids:
            if ast < 0:
                while st and st[-1] > 0 and st[-1] < abs(ast):
                    st.pop()
                
                if st and st[-1] == abs(ast):
                    st.pop()
                    continue
                
                if not st or st[-1] < 0:
                    st.append(ast)
                
            else:
                st.append(ast)
        
        return st