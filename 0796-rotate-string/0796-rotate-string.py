class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        for _ in range(len(s)):
            s = s[1:] + s[0]
            if goal == s:
                return True

        return False