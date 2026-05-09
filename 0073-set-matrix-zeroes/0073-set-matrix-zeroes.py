class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row = ['#'] * m
        col = ['#'] * n

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row[r] = 0
                    col[c] = 0

        for r in range(m):
            if row[r] == 0:
                for c in range(n):
                    matrix[r][c] = 0
        
        for c in range(n):
            if col[c] == 0:
                for r in range(m):
                    matrix[r][c] = 0
        
        return matrix