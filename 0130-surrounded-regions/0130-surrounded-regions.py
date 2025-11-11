class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        # process top and bottom row
        for j in range(cols):
            # top row
            if board[0][j] == 'O':
                dfs(0, j)
            # bottom row
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        # process left and right column
        for i in range(rows):
            # left col
            if board[i][0] == 'O':
                dfs(i, 0)
            # right col
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
            
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'