class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left=0
        right=0
        maxLength=0
        while right < len(s):
            if s[right] not in substring:
                substring.add(s[right])
                if len(substring) > maxLength: maxLength = len(substring)
                right+=1
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left+=1

        return maxLength