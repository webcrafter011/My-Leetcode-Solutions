class DisjointSet:
    def __init__(self, n):
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i
        self.rank = [0] * n

    def find_par(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find_par(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ulp_u = self.find_par(u)
        ulp_v = self.find_par(v)

        if ulp_u == ulp_v:
            return 
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_row = max_col = 0
        for u, v in stones:
            max_row = max(max_row, u)
            max_col = max(max_col, v)

        ds = DisjointSet(max_row + max_col + 2)
        nodes = set()
        for u, v in stones:
            ds.union_by_rank(u, v + max_row + 1)
            nodes.add(u)
            nodes.add(v + max_row + 1)
        
        components = 0
        for node in nodes:
            if node == ds.find_par(node):
                components += 1
        
        return len(stones) - components
