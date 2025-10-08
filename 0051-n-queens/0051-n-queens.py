class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # helper funtion
        def isSafe1(row, col, board):
            r = row
            c = col

            # check anti clock diagonal
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            
            r = row
            c = col
            # check left side
            while c >= 0:
                if board[r][c] == 'Q':
                    return False
                c -= 1
            
            r = row
            c = col
            # check clockwise diagonal
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1
            
            return True

        # backtracking function
        def backtrack(col, board, ans):
            if col == n:
                ans.append(board.copy())
                return
            
            for row in range(n):
                if isSafe1(row, col, board):
                    board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                    backtrack(col + 1, board, ans)
                    board[row] = board[row][:col] + '.' + board[row][col + 1:]
            
        ans = []
        backtrack(0, ['.'*n for _ in range(n)], ans)
        return ans