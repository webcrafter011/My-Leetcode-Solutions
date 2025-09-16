class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = rightSum = 0

        for i in range(k):
            leftSum += cardPoints[i]
        
        maxSum = leftSum
        for i in range(k):
            leftSum -= cardPoints[k - 1 - i]
            rightSum += cardPoints[(len(cardPoints) - 1) - i]
            maxSum = max(maxSum, leftSum + rightSum)
        
        return maxSum