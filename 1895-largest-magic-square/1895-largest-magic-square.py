class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # takes top left and bottom right coordinates are args
        def row_sum_equals(row_start, row_end, col_start, col_end):
            # grid[1][1:4]
            prev = 0
            for j in range(col_start, col_end + 1):
                prev += grid[row_start][j]
            
            for i in range(row_start + 1, row_end + 1):
                curr_sum = 0
                for j in range(col_start, col_end + 1):
                    curr_sum += grid[i][j]
                if prev != curr_sum:
                    return (False, prev)
            
            return (True, prev)
        
        def col_sum_equals(row_start, row_end, col_start, col_end):
            prev = 0
            for i in range(row_start, row_end + 1):
                prev += grid[i][col_start]
            
            for j in range(col_start + 1, col_end + 1):
                curr_sum = 0
                for i in range(row_start, row_end + 1):
                    curr_sum += grid[i][j]
                if prev != curr_sum:
                    return (False, prev)
            
            return (True, prev)
        
        def dig_sum_equals(row_start, row_end, col_start, col_end):
            left_to_right = 0
            range1 = range(row_start, row_end + 1)
            range2 = range(col_start, col_end + 1)
            for i, j in zip(range1, range2):
                left_to_right += grid[i][j]
            
            right_to_left = 0
            range1 = range(row_start, row_end + 1)
            range2 = range(col_end, col_start - 1, -1)
            for i, j in zip(range1, range2):
                right_to_left += grid[i][j]
            
            return (left_to_right == right_to_left, left_to_right)
        

        max_side = 1
        n, m = len(grid), len(grid[0])

        for row_start in range(n):
            for col_start in range(m):
                row_end = row_start + 1
                col_end = col_start + 1
                while row_end < n and col_end < m:
                    rows = row_sum_equals(row_start, row_end, col_start, col_end)
                    cols = col_sum_equals(row_start, row_end, col_start, col_end)
                    digs = dig_sum_equals(row_start, row_end, col_start, col_end)
                    if (
                        rows[0] and
                        cols[0] and
                        digs[0] and
                        rows[1] == cols[1] == digs[1]
                    ):
                        max_side = max(max_side, (row_end - row_start) + 1)
                    row_end += 1
                    col_end += 1
    
        return max_side
                    
