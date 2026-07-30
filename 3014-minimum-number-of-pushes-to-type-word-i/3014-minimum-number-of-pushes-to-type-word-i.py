class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        n = len(word)
        div = n // 8
        rem = n % 8

        ans += (rem * (div + 1))

        while div:
            ans += (8 * div)
            div -= 1
        
        return ans
        
