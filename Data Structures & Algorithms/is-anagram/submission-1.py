class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1 = dict()
        for letter in s:
            if letter in hash_map1:
                hash_map1[letter] +=1
            else:
                hash_map1[letter] =1


        hash_map2 = dict()
        for letter in t:
            if letter in hash_map2:
                hash_map2[letter] +=1
            else:
                hash_map2[letter] =1

        if(hash_map2==hash_map1):
            return True
        else:
            return False