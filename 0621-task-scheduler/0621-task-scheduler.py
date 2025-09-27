class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        f = max(freq.values())
        count_max = 0
        for val in freq.values():
            if val == f:
                count_max += 1
        
        return max(len(tasks), (f - 1) * (n + 1) + count_max)