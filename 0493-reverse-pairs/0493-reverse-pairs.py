class Solution(object):
    def reversePairs(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.mergeSort(arr, 0, len(arr) - 1)

    def mergeSort(self, arr, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        
        count = 0

        count += self.mergeSort(arr, l, mid)
        count += self.mergeSort(arr, mid + 1, r)

        count += self.merge(arr, l, mid, r)
    
        return count
    
    def merge(self, arr, l, mid, r):
        count = 0

        j = mid + 1
        for i in range(l, mid + 1):
            while j <= r and arr[i] > 2 * arr[j]:
                j += 1
            count += j - (mid + 1)

        temp = []
        left, right = l, mid + 1

        while left <= mid and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= r:
            temp.append(arr[right])
            right += 1

        arr[l:r+1] = temp

        return count 
        
        
                        