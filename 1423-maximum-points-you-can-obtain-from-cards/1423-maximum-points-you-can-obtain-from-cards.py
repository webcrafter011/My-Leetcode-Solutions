class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = maxi = sum(cardPoints[:k])
        n = len(cardPoints)

        for i in range(k):
            curr -= cardPoints[k - i - 1]
            curr += cardPoints[n - 1 - i]

            maxi = max(curr, maxi)
        
        return maxi