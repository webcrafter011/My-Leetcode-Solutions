class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # using dfs 

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        for r in range(m):
            for c in range(n):

                if grid[r][c] != 0 and not visited[r][c]:
                    q = deque([[r, c]])
                    visited[r][c] = True
                    curr_sum = 0

                    while q:
                        i, j = q.popleft()
                        curr_sum += grid[i][j]

                        for x, y in directions:
                            row, col = i + x, j + y

                            if 0 <= row < m and 0 <= col < n:
                                if grid[row][col] and not visited[row][col]:
                                    
                                    visited[row][col] = True
                                    q.append([row, col])
                    
                    if curr_sum % k == 0:
                        count += 1
        
        return count
