class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        st = []
        n = len(heights)

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                el = st[-1]
                nse = i
                st.pop()
                pse = st[-1] if st else -1
                area = (nse - pse - 1) * heights[el]
                maxArea = max(maxArea, area)
            
            st.append(i)
        
        while st:
            el = st[-1]
            nse = n
            st.pop()
            pse = st[-1] if st else -1
            area = (nse - pse - 1) * heights[el]
            maxArea = max(maxArea, area)

        return maxArea