class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_ones = []
        col_ones = []

        # count ones in each row
        for row in mat:
            curr_ones = 0
            for num in row: 
                if num == 1:
                    curr_ones += 1
            row_ones.append(curr_ones)
        
        # count ones in each column
        for j in range(n):
            curr_ones = 0
            for i in range(m):
                if mat[i][j] == 1:
                    curr_ones += 1
            col_ones.append(curr_ones)
        
        # calculate special pos
        specials = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_ones[i] == 1 and col_ones[j] == 1:
                    specials += 1
        
        return specials
