class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        NGE = {}
        st = []

        for i in range(n - 1, -1, -1):
            while st and st[-1] < nums2[i]:
                st.pop()

            NGE[nums2[i]] = st[-1] if st else -1

            st.append(nums2[i])
        
        return [NGE[num] for num in nums1]