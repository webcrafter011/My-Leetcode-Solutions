class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # maxSum = 0
        # n = len(cardPoints)
        # for i in range(k + 1):
        #     left_sum = sum(cardPoints[:i])
        #     right_sum = sum(cardPoints[n - (k - i):])
        #     maxSum = max(maxSum, left_sum + right_sum)
        
        # return maxSum

        right_sum = 0
        maxSum = 0
        n = len(cardPoints)

        for i in range(k):
            right_sum += cardPoints[i]
            maxSum = max(right_sum, maxSum)
        
        left_sum = 0
        for j in range(k):
            right_sum -= cardPoints[k - j - 1]
            left_sum += cardPoints[n - j - 1]
            maxSum = max(maxSum, right_sum + left_sum)
        
        return maxSum