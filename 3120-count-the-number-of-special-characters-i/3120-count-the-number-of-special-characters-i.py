class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        count = 0

        for c in word:
            if c.islower() and c.upper() in word:
                count += 1
        
        return count
                