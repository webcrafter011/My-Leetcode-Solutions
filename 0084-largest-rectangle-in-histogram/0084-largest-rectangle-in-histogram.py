class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # # Next Smaller Elements
        # NSE = [n] * n
        # st = []
        # for i in range(n - 1, -1, -1):
        #     while st and heights[st[-1]] >= heights[i]:
        #         st.pop()
        #     NSE[i] = st[-1] if st else n
        #     st.append(i)
        
        # # Previous Smaller Elements
        # PSE = [-1] * n
        # st = []
        # for i in range(n):
        #     while st and heights[st[-1]] > heights[i]:
        #         st.pop()
        #     PSE[i] = st[-1] if st else -1
        #     st.append(i)

        # max_area = float('-inf')
        # for i in range(n):
        #     area = heights[i] * (NSE[i] - PSE[i] - 1)
        #     max_area = max(max_area, area)
        
        # return max_area

        # Most optimal approach
        maxArea = float('-inf')
        st = []
        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                element = st[-1]
                st.pop()
                nse = i
                pse = st[-1] if st else -1
                maxArea = max(maxArea, (nse - pse - 1) * heights[element])
            
            st.append(i)

        while st:
            nse = n
            element = st[-1]
            st.pop()
            pse = st[-1] if st else -1
            maxArea = max(maxArea, (nse - pse - 1) * heights[element])
        
        return maxArea