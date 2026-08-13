class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        count = 0
        while start or goal:
            if ((start & 1) ^ (goal & 1)):
                count += 1
            start = start >> 1
            goal = goal >> 1
        
        return count
