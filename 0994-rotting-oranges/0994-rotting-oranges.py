class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((0, i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        while q:
            curr_time, i, j = q.popleft()
            time = curr_time
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((time + 1, nr, nc))
                    fresh -= 1
        
        return time if fresh == 0 else -1