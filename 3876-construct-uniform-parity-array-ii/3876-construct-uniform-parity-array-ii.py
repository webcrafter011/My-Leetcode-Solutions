class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        same_parity = False
        even = nums1[0] % 2 == 0
        
        if even:
            uniform = True
            for num in nums1:
                if not num % 2 == 0:
                    uniform = False
                    break
            if uniform:
                return True
        else:
            uniform = True
            for num in nums1:
                if not num % 2:
                    uniform = False
                    break
            if uniform:
                return True

        mini = min(nums1)
        return mini % 2 == 1