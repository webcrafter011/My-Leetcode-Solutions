class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        reverse = forward = startIndex
        n = len(words)

        for _ in range(n):
            if words[forward % n] == target:
                return abs(forward - startIndex)
            elif words[(reverse + n ) % n] == target:
                return abs(reverse - startIndex) 
            forward += 1
            reverse -= 1
        
        return -1