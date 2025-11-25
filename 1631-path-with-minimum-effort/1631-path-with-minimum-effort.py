class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        heap = [(0, 0, 0)] # (effort, row, column)

        while heap:
            effort, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return effort
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    edge_weight = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, edge_weight)
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
                
            
        return -1