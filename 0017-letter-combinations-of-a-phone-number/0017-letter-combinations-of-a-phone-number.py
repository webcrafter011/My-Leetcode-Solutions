class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        n = len(digits)

        def build(i, arr):
            if i == n:
                res.append(''.join(arr))
                return 
        
            for char in digit_to_letters[digits[i]]:
                arr.append(char)
                build(i + 1, arr)
                arr.pop()
        
        build(0, [])
        return res

            
