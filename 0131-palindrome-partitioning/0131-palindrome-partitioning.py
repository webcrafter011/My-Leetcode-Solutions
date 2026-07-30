class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        partitions = []

        def backtrack(start, path):
            if start == len(s):
                partitions.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if substr == substr[::-1]:
                    path.append(substr)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return partitions