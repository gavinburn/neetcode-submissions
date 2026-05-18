class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashMap1 = {}
        hashMap2 = {}

        for letter in t:
            if letter in hashMap1:
                hashMap1[letter]+=1
            else:
                hashMap1[letter]=1

        leftPointer=0
        rightPointer=0
        matches=0
        minSize=10000
        firstTime=True
        res = ""

        while rightPointer < len(s) and leftPointer < len(s):
            if s[leftPointer] not in hashMap1:
                leftPointer+=1
            else:
                if firstTime:
                    rightPointer=leftPointer
                    firstTime=False
                if s[leftPointer] not in hashMap2:
                    hashMap2[s[leftPointer]] = 1
                    matches += 1
                while matches < len(t) and rightPointer + 1 < len(s):
                    rightPointer+=1
                    if s[rightPointer] in hashMap1:
                        if s[rightPointer] in hashMap2 and hashMap2[s[rightPointer]] != 0:
                            if hashMap1[s[rightPointer]] > hashMap2[s[rightPointer]]:
                                matches+=1
                            hashMap2[s[rightPointer]] +=1
                        else:
                            hashMap2[s[rightPointer]]=1
                            matches+=1
                if matches == len(t):
                    if rightPointer-leftPointer < minSize:
                        minSize = (rightPointer-leftPointer)+1
                        res = s[leftPointer: rightPointer+1]
                hashMap2[s[leftPointer]]-=1
                if hashMap2[s[leftPointer]] < hashMap1[s[leftPointer]]:
                    matches -= 1
                leftPointer+=1

        return res