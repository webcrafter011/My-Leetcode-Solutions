class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        n = len(s)

        for i in range(n):
            # 1. counts per letter
            counts = [0] * 26
            # 2. how many letters have a given frequency
            freq_of_freq = {0: 26}  # initially 26 letters with freq 0
            max_f = 0
            min_f = float('inf')

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                old_c = counts[idx]
                new_c = old_c + 1
                counts[idx] = new_c

                # update freq_of_freq
                freq_of_freq[old_c] -= 1
                if freq_of_freq[old_c] == 0:
                    del freq_of_freq[old_c]
                freq_of_freq[new_c] = freq_of_freq.get(new_c, 0) + 1

                # update max_f
                if new_c > max_f:
                    max_f = new_c

                # update min_f:
                # - if this is the first non-zero freq, set min_f=new_c
                # - else, if new_c < min_f, use it
                # - else, if old_c was the only letter at min_f and we removed it, bump min_f up one
                if new_c == 1 and len(freq_of_freq) == 1:
                    # only one freq in the map
                    min_f = 1
                else:
                    if new_c < min_f:
                        min_f = new_c
                    elif old_c == min_f and old_c not in freq_of_freq:
                        # our old min disappeared, must find the next smallest key
                        min_f = min(k for k in freq_of_freq.keys() if k > 0)

                total += (max_f - min_f)

        return total
