class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer=0
        rightPointer=0
        charSet = set()
        maxLen=0

        while rightPointer< len(s):
            while s[rightPointer] in charSet:
                charSet.remove(s[leftPointer])
                leftPointer+=1
            else:
                charSet.add(s[rightPointer])
                if len(charSet)>maxLen: maxLen=len(charSet)
                rightPointer+=1

        return maxLen