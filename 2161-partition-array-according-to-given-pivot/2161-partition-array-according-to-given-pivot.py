class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = 0
        equal = 0
        larger = 0

        for num in nums:
            if num < pivot:
                smaller += 1
            elif num > pivot:
                larger += 1
            else:
                print(f'num={num}, pivot={pivot}')
                equal += 1
        
        first_smaller = 0
        first_equal = smaller
        first_larger = smaller + equal

        print(first_smaller, first_equal, first_larger)

        ans = [-1] * len(nums)

        for num in nums:
            if num < pivot:
                ans[first_smaller] = num
                first_smaller += 1
            elif num > pivot:
                ans[first_larger] = num
                first_larger += 1
            else:
                ans[first_equal] = num
                first_equal += 1
        
        return ans