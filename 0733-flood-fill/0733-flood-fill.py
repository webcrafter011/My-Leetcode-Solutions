class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        og_color = image[sr][sc]
        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == og_color:
                    q.append((nr, nc))
        
        return image
