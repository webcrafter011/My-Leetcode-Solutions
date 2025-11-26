from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # cost to reach each node
        dist = [float('inf')] * n
        dist[src] = 0
        
        q = deque()
        q.append((src, 0, 0))  # node, cost, stops
        
        while q:
            node, cost, stops = q.popleft()
            
            if stops > k:
                continue
            
            for nei, w in adj[node]:
                new_cost = cost + w
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    q.append((nei, new_cost, stops + 1))
        
        return dist[dst] if dist[dst] != float('inf') else -1
