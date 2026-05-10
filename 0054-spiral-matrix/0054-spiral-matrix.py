class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        t, l = 0, 0
        b, r = len(matrix) - 1, len(matrix[0]) - 1

        spiral = []

        while t <= b and l <= r:

            for i in range(l, r + 1):
                spiral.append(matrix[t][i])
            t += 1

            for i in range(t, b + 1):
                spiral.append(matrix[i][r])
            r -= 1

            if t <= b:
                for i in range(r, l - 1, -1):
                    spiral.append(matrix[b][i])
                b -= 1

            if l <= r:
                for i in range(b, t - 1, -1):
                    spiral.append(matrix[i][l])
                l += 1
            
        
        return spiral