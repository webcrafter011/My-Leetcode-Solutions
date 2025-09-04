class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge_map = {}
        st = []
        
        for num in nums2:
            while st and st[-1] < num:
                nge_map[st.pop()] = num
            st.append(num)
        
        for num in st:
            nge_map[num] = -1
        
        return [nge_map[num] for num in nums1]