class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # maxCount = 0
        # n = len(fruits)

        # for i in range(n):
        #     basket = {}
        #     for j in range(i, n):
        #         fruit = fruits[j]
        #         basket[fruit] = basket.get(fruit, 0) + 1

        #         if len(basket) > 2:
        #             break
                
        #         maxCount = max(maxCount, j - i + 1)

        # return maxCount
        
        l = r = 0
        maxLen = 0
        h = {}

        while r < len(fruits):
            h[fruits[r]] = h.get(fruits[r], 0) + 1

            if len(h) > 2:
                h[fruits[l]] -= 1
                if h[fruits[l]] == 0:
                    del h[fruits[l]]
                l += 1

            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen