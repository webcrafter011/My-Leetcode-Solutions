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
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet(n)
        extra_edges = 0

        for u, v in edges:
            if ds.find_par(u) == ds.find_par(v):
                extra_edges += 1
            else:
                ds.union_by_size(u, v)
        
        components = set()
        for node in range(n):
            components.add(ds.find_par(node))

        ans = len(components) - 1
        if extra_edges >= ans:
            return ans
        else: 
            return -1
