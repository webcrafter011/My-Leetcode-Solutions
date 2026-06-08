class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])

        def get_max(row):
            max_el = float('-inf')
            index = -1

            for i in range(m):
                if max_el < mat[row][i]:
                    max_el = mat[row][i]
                    index = i


            return [max_el, index]


        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            max_el, col = get_max(mid)

            up = mat[mid - 1][col] if mid > 0 else -1
            down = mat[mid + 1][col] if mid < n - 1 else - 1

            if up < max_el > down:
                return [mid, col]
            elif down > max_el:
                low = mid + 1
            elif up > max_el:
                high = mid - 1
        
        return [-1, -1]




