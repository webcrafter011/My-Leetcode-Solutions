class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indeg = [0] * n
        rev_adj = {val:[] for val in range(n)}

        for i in range(n):
            for child in graph[i]:
                indeg[i] += 1
                rev_adj[child].append(i)
        
        q = deque()
        for node in range(n):
            if indeg[node] == 0:
                q.append(node)

        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in rev_adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return sorted(res)

