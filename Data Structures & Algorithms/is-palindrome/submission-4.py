class Solution:

    def isAlphaNum(self, letter):
        if letter.isalpha() or letter.isdigit():
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        backIndex = len(s) - 1
        frontIndex = 0
        for i, letter in enumerate(s):

            # Check if the character at frontIndex is alphanumeric or not a space
            while(self.isAlphaNum(s[frontIndex]) == False or s[frontIndex] == " "):
                frontIndex += 1
                if frontIndex >= backIndex:
                    break

            # Check if the character at backIndex is alphanumeric or not a space
            while(self.isAlphaNum(s[backIndex]) == False or s[backIndex] == " "):
                backIndex -= 1
                if frontIndex >= backIndex:
                    break

            if frontIndex >= backIndex:
                break

            # Convert to lowercase if it's uppercase
            if s[frontIndex].isupper():
                s = s[:frontIndex] + s[frontIndex].lower() + s[frontIndex + 1:]

            if s[backIndex].isupper():
                s = s[:backIndex] + s[backIndex].lower() + s[backIndex + 1:]

            # Compare the characters at frontIndex and backIndex
            if s[frontIndex] != s[backIndex]:
                return False

            frontIndex += 1
            backIndex -= 1

        return True