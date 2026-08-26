class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        # next greater element
        NGE = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            
            NGE[i] = st[-1] if st else n
            st.append(i)

        # previous greater element
        PGE = [-1] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            
            PGE[i] = st[-1] if st else -1
            st.append(i)

        # next smaller element
        NSE = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            
            NSE[i] = st[-1] if st else n
            st.append(i)
        
        # previous smaller element
        PSE = [-1] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            
            PSE[i] = st[-1] if st else -1
            st.append(i)
        
        # final calculation for each element
        # we will calculate maximum and minimum calculation of each element in all the subarrays it will occur then we will substract each contribution maxi - mini
        res = 0
        for i in range(n):
            # maximum contribution 
            left = i - PGE[i]
            right = NGE[i] - i
            max_contri = nums[i] * left * right

            # minimum contribution 
            left = i - PSE[i]
            right = NSE[i] - i
            min_contri = nums[i] * left * right

            res += max_contri - min_contri
        
        return res