class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = ""
        longest = ""

        for i, letter in enumerate(s):
            curr = letter
            left = i-1
            right = i+1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    curr = s[left] + curr + s[right]
                    left-=1
                    right+=1
                else:
                    break
            if len(curr) > len(longest):
                longest = curr

            curr = ""
            left = i
            right = i+1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    curr = s[left] + curr + s[right]
                    left-=1
                    right+=1
                else:
                    break

            if len(curr) > len(longest):
                longest = curr
            curr = ""

        return longest

            



        