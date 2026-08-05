class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in invocations:
            graph[a].append(b)
        
        sus = [False] * n

        def dfs(method):
            sus[method] = True

            for nei in graph[method]:
                if not sus[nei]:
                    dfs(nei)
        
        dfs(k)

        # if any non suspicious method calls a suspicious method then return whole list as is 
        for caller, called in invocations:
            if not sus[caller] and sus[called]:
                return list(range(n))

        return [
            method for method in range(n) 
            if not sus[method]
        ]
        
