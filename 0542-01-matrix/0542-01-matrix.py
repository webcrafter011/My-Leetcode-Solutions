class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        res = [[-1] * cols for _ in range(rows)]
        q = deque([])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                    res[i][j] = 0
        
        while q:
            row, col = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + row, dc + col
                if 0 <= nr < rows and 0 <= nc < cols and res[nr][nc] == -1:
                    res[nr][nc] = res[row][col] + 1
                    q.append((nr, nc))
        
        return res