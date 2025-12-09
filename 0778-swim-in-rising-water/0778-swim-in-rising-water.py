class DisjointSet:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        for i in range(len(self.parent)):
            self.parent[i] = i
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
    
    def find_par(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_par(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self, u, v):
        ultp_u = self.find_par(u)
        ultp_v = self.find_par(v)
        
        if ultp_u == ultp_v:
            return
        if self.rank[ultp_u] < self.rank[ultp_v]:
            self.parent[ultp_u] = ultp_v
        elif self.rank[ultp_u] > self.rank[ultp_v]:
            self.parent[ultp_v] = ultp_u
        else:
            self.parent[ultp_v] = ultp_u
            self.rank[ultp_u] += 1
    
    def union_by_size(self, u, v):
        ultp_u = self.find_par(u)
        ultp_v = self.find_par(v)
        
        if ultp_u == ultp_v:
            return
        if self.size[ultp_u] < self.size[ultp_v]:
            self.parent[ultp_u] = ultp_v
            self.size[ultp_v] += self.size[ultp_u]
        else:
            self.parent[ultp_v] = ultp_u
            self.size[ultp_u] += self.size[ultp_v]
        
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DisjointSet(n*n)
        cells = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        open_cells = [[False] * n for _ in range(n)]

        def index(r, c):
            return r * n + c

        for r in range(n):
            for c in range(n):
                cells.append((grid[r][c], r, c))
        
        cells.sort(key = lambda x: x[0])

        for h, r, c in cells:
            open_cells[r][c] = True
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and open_cells[nr][nc]:
                    dsu.union_by_rank(index(r, c), index(nr, nc))
            
            if dsu.find_par(0) == dsu.find_par(n * n - 1):
                return h



