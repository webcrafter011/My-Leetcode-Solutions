class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = [abs(num) for num in nums]
        arr.sort()

        i, j = 0, len(arr) - 1
        res = 0

        while i <= j:
            if i == j:
                res += (arr[j] * arr[j])
                break
            
            res += arr[j] * arr[j]
            res -= arr[i] * arr[i]

            i += 1
            j -= 1
        
        return res