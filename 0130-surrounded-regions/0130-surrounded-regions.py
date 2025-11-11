class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def bfs(r, c):
            q = deque([(r, c)])

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()
                if board[r][c] != 'O':
                    continue
                else:
                    board[r][c] = 'T'

                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                        q.append((row, col))



        # process top and bottom row
        for j in range(cols):
            # top row
            if board[0][j] == 'O':
                bfs(0, j)
            # bottom row
            if board[rows - 1][j] == 'O':
                bfs(rows - 1, j)

        # process left and right column
        for i in range(rows):
            # left col
            if board[i][0] == 'O':
                bfs(i, 0)
            # right col
            if board[i][cols - 1] == 'O':
                bfs(i, cols - 1)
            
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'