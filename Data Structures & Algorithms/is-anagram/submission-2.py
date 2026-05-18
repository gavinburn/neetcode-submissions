class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        for letter in s:
            if letter in hashMap1:
                hashMap1[letter] +=1
            else: hashMap1[letter] = 1

        for letter2 in t:
            if letter2 in hashMap2:
                hashMap2[letter2] +=1
            else: hashMap2[letter2] = 1

        if hashMap1==hashMap2: return True
        else: return False