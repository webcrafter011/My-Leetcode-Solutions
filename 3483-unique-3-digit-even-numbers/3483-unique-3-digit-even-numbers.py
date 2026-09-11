class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        n = len(digits)
        nums = set()

        for i in range(n):
            # skip if odd
            if digits[i] % 2:
                continue
            
            # if even digit, check all possibilities
            for j in range(n):
                if j == i:
                    continue    
                
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    curr = str(digits[j]) + str(digits[k]) + str(digits[i])

                    curr = int(curr)

                    if len(str(curr)) < 3:
                        continue

                    if curr not in nums:
                        nums.add(curr)
                        count += 1
                                            
                    
        return count


                