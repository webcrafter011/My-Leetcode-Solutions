class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def add_result(res, board):
            copy = []
            for row in board:
                cur = ''.join(row)
                copy.append(cur)
            res.append(copy)

        def build(row, board):
            if row == n:
                add_result(res, board)
                return 
            
            for col in range(n):
                if (
                    col in cols 
                    or row - col in diag1 
                    or row + col in diag2
                ):
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # explore next row
                build(row + 1, board)

                # backtrack by removing all the values in sets and existing queen
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
            
        build(0, board)
        return res

                