from typing import List
from collections import defaultdict
import bisect

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def flip(x: int) -> int:
            return int(str(x)[::-1])

        # build map value -> sorted list of indices where it appears
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)

        best = float('inf')
        for i, v in enumerate(nums):
            r = flip(v)
            if r not in positions:
                continue
            idx_list = positions[r]
            
            jpos = bisect.bisect_right(idx_list, i) 
            if jpos < len(idx_list):
                j = idx_list[jpos]
                best = min(best, j - i)

        return best if best != float('inf') else -1
