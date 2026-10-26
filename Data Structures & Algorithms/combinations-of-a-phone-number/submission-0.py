class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        curr = []
        output = []

        if digits == "":
            return []

        def recurse(level):

            if level >= len(digits):
                toAdd = curr.copy()
                output.append("".join(toAdd))
                return

            for letter in digitToChar[digits[level]]:
                curr.append(letter)
                recurse(level+1)

                curr.pop()

        recurse(0)
        return output