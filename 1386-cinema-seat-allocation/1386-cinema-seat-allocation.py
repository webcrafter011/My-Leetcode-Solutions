from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res_rows = defaultdict(set)

        for row, seat in reservedSeats:
            res_rows[row].add(seat)

        def group_can_seat(r, i, j, res_rows):
            for i in range(i, j):
                if i in res_rows[r]:
                    return False
                
            return True
            
        count = 0
        for r in res_rows:
            fv = group_can_seat(r, 2, 6, res_rows)
            sv = group_can_seat(r, 4, 8, res_rows)
            tv = group_can_seat(r, 6, 10, res_rows)

            if fv and tv:
                count += 2
            elif fv or sv or tv:
                count += 1                   


        count += (n - len(res_rows)) * 2
        return count