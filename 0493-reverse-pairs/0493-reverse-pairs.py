class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge_sort(arr, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            cnt = merge_sort(arr, low, mid)
            cnt += merge_sort(arr, mid + 1, high)

            # count reverse pairs before merging
            right = mid + 1
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                cnt += (right - (mid + 1))

            # standard merge
            merge(arr, low, mid, high)
            return cnt

        def merge(arr, low, mid, high):
            temp = []
            left, right = low, mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left]); left += 1
            while right <= high:
                temp.append(arr[right]); right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        return merge_sort(nums, 0, len(nums) - 1)