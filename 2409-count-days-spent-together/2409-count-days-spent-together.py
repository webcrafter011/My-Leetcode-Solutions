class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def get_index(date):
            month, day = date.split('-')
            res = 0

            for i in range(int(month) - 1):
                res += days_in_months[i]
            
            res += int(day)
            return res
        
        alice_start, alice_end = get_index(arriveAlice), get_index(leaveAlice)
        bob_start, bob_end = get_index(arriveBob), get_index(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)
    
        return max(0, end - start + 1)