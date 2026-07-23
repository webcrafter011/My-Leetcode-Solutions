class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        n = len(s)
        i = 0

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Check optional sign
        sign = 1

        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        def convert(index: int, number: int) -> int:
            # Stop at end or first non-digit
            if index == n or not s[index].isdigit():
                return number * sign

            digit = int(s[index])

            # Check overflow before adding the digit
            if number * 10 + digit > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN

            return convert(index + 1, number * 10 + digit)

        return convert(i, 0)