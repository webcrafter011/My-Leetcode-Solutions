class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])

        sorted_queries = sorted(
            enumerate(queries),
            key=lambda q: q[1]
        )

        res = [0] * len(queries)
        freq = {}
        left = right = 0

        for idx, q in sorted_queries:

            # Add logs with timestamp <= q
            while right < len(logs) and logs[right][1] <= q:
                s, t = logs[right]
                freq[s] = freq.get(s, 0) + 1
                right += 1

            # Remove logs with timestamp < q - x
            while left < right and logs[left][1] < q - x:
                s, t = logs[left]

                freq[s] -= 1

                if freq[s] == 0:
                    del freq[s]

                left += 1

            res[idx] = n - len(freq)

        return res