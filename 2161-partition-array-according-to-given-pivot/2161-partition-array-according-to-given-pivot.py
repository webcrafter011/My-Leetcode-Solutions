class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        larger = []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                larger.append(num)
            else:
                equal.append(num)
        
        ans = []

        ans.extend(smaller)
        ans.extend(equal)
        ans.extend(larger)

        return ans