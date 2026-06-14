class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}

        for c in s:
            counter[c] = counter.get(c, 0) + 1

        # key value paits [char, count]

        counts = []
        for char in counter:
            counts.append([char, counter[char]])
        
        counts.sort(reverse=True, key=lambda x:x[1])

        ans = ''

        for char, count in counts:
            ans += (char) * count
        
        return ans