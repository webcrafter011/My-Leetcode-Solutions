class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        def dfs(node, parent):
            nonlocal timer
            visited.add(node)
            tin[node] = low[node] = timer
            timer += 1

            for nei in adj[node]:
                if parent == nei:
                    continue
                if nei not in visited:
                    dfs(nei, node)
                    low[node] = min(low[nei], low[node])
                    if low[nei] > tin[node]:
                        bridges.append((nei, node))
                else:
                    low[node] = min(low[nei], low[node])
        
        adj = defaultdict(list)
        for u, v  in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        bridges = []
        timer = 1
        tin = [0] * n
        low = [0] * n
        for node in range(n):
            if node not in visited:
                dfs(node, -1)

        return bridges