class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        positions = {}

        for i, c in enumerate(word):
            if c.islower():
                positions[c] = i
            elif c.isupper() and c not in positions:
                positions[c] = i
        
        count = 0
        seen = set()

        for c in word:
            if c.islower() and c not in seen and c.upper() in positions:
                if positions[c] < positions[c.upper()]:
                    count += 1
                    seen.add(c)
        
        return count
