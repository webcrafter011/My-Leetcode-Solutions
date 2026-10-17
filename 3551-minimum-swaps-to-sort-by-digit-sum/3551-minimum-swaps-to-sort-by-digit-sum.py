class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        arr = sorted(
            [(sum(map(int, str(num))), num, i) for i, num in enumerate(nums)]
        )

        visited = [False] * n
        res = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            res += cycle_size - 1

        return res