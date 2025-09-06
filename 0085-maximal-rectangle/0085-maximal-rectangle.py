class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        preSum = [[0] * m for _ in range(n)]

        # calculating the presum map to recreate the histogram structure
        for j in range(m):
            for i in range(n):
                if matrix[i][j] == '1':
                    preSum[i][j] = preSum[i - 1][j] + 1 if i > 0 else 1
                else:
                    preSum[i][j] = 0
        
        # calculating max histogram area by taking each row as x-axis

        maxArea = 0
        for row in preSum:
            st = []
            for i in range(m):
                while st and row[st[-1]] > row[i]:
                    element = st[-1]
                    nse = i
                    st.pop()
                    pse = st[-1] if st else -1
                    area = row[element] * (nse - pse - 1)
                    maxArea = max(maxArea, area)
                
                # append current index in stack
                st.append(i)
            
            while st:
                element = st[-1]
                nse = m
                st.pop()
                pse = st[-1] if st else -1
                area = row[element] * (nse - pse - 1)
                maxArea = max(maxArea, area)
            
        return maxArea

