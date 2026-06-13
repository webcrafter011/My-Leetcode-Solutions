class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''

        for word in words:
            curr_wt = 0
            for c in word:
                curr_wt += weights[ord(c) - 97]
            curr_wt %= 26

            ans += chr((25 - curr_wt) + 97)

        return ans