class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        i = j = 0
        switch = True
        for i in range(len(nums)):
            if switch:
                nums[i] = pos[j]
                switch = False
            else:
                nums[i] = neg[j]
                j += 1
                switch = True
        
        return nums