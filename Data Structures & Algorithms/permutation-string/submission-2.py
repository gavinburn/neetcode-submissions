class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_1 = {}
        map_2 = {}
        i = 97
        while i < 123:
            map_1[chr(i)] = 0
            map_2[chr(i)] = 0
            i += 1

        leftPointer=0
        rightPointer=0

        while rightPointer < len(s1) and rightPointer < len(s1):
            map_1[s1[rightPointer]]+=1
            if rightPointer < len(s2):
                map_2[s2[rightPointer]]+=1
            else: return False
            rightPointer+=1

        if map_2 == map_1: return True

        while rightPointer < len(s2):
            map_2[s2[rightPointer]]+=1
            rightPointer+=1
            map_2[s2[leftPointer]]-=1
            leftPointer+=1
            if map_2 == map_1: return True
        return False