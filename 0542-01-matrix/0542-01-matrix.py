class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[-1] * n for _ in range(m)]

        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    q.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < m and 0 <= col < n and res[row][col] == -1:
                    res[row][col] = res[r][c] + 1
                    q.append((row, col))

        return res