class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        baskets = {}
        maxLen = 0

        for right in range(len(fruits)):
            baskets[fruits[right]] = baskets.get(fruits[right], 0) + 1

            if len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen