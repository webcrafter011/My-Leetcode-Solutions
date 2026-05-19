class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for line in range(1, numRows):
            last_row = triangle[-1]
            res = [1]
            prev = 1
            i = 1

            while i < line:
                res.append(last_row[i] + prev)
                prev = last_row[i]
                i += 1
            
            res.append(1)
            triangle.append(res)
        
        return triangle