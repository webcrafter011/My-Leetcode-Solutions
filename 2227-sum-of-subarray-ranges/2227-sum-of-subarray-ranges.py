class Solution:
    def subArrayRanges(self, arr: List[int]) -> int:
        # bruteforce solution O(n^2)
        # n = len(nums)
        # total = 0

        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         arr = nums[i:j]
        #         total += max(arr) - min(arr)
        
        # return total

        # optimal approach
        # calculate next greater elements indices
        n = len(arr)

        # Previous Less Element
        PLE = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            PLE[i] = stack[-1] if stack else -1
            stack.append(i)

        # Next Less Element
        NLE = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            NLE[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Next Greater Element
        NGE = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            NGE[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Previoius Greater Element
        PGE = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            PGE[i] = stack[-1] if stack else -1
            stack.append(i)
        


        res = 0
        for i in range(n):
            # For minimums
            left_min = i - PLE[i]
            right_min = NLE[i] - i
            min_contribution = arr[i] * left_min * right_min

            # For maximums
            left_max = i - PGE[i]
            right_max = NGE[i] - i
            max_contribution = arr[i] * left_max * right_max

            # Combine both
            res = (res + max_contribution - min_contribution)

        return res
