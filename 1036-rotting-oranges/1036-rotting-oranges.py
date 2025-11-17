class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0)) # row, column, time = 0 to begin
                elif grid[i][j] == 1:
                    fresh += 1 # count the number of fresh oranges

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        while q:
            r, c, minute = q.popleft()
            time = max(time, minute)
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                    grid[row][col] = 2
                    q.append((row, col, time + 1))
                    fresh -= 1
        
        return time if fresh == 0 else -1

            