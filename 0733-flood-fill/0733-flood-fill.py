class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(sr, sc)])
        og_color = image[sr][sc]

        while q:
            pr, pc = q.popleft()
            image[pr][pc] = color
            for dr, dc in directions:
                row, col = dr + pr, dc + pc
                if 0 <= row < rows and 0 <= col < cols and image[row][col] == og_color:
                    q.append((row, col))

        return image
