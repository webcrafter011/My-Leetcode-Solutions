class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(course, path):
            if course in path:
                return False
            if course in vis:
                return True
            
            vis.add(course)
            path.add(course)

            for next_course in adj[course]:
                if not dfs(next_course, path):
                    return False
            
            path.remove(course)
            return True

        vis = set()
        for i in range(numCourses):
            if i not in vis:
                path = set()
                if not dfs(i, path):
                    return False
        
        return True
                