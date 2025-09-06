class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        preSum = [[0] * m for _ in range(n)]

        for j in range(m):
            for i in range(n):
                if matrix[i][j] == '1':
                    preSum[i][j] = preSum[i - 1][j] + 1 if i > 0 else 1
                else:
                    preSum[i][j] = 0
        
        maxArea = 0
        for heights in preSum:
            st = []
            for i in range(m):
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
                nse = m
                st.pop()
                pse = st[-1] if st else -1
                area = (nse - pse - 1) * heights[el]
                maxArea = max(maxArea, area)
                
        return maxArea

