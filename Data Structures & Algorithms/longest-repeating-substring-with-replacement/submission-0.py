class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        leftPointer=0
        rightPointer=0
        hash_map={}
        largestNum=0
        largestLetter=""
        subString=0
        while rightPointer<len(s):
            if s[rightPointer] in hash_map:
                hash_map[s[rightPointer]]+=1
            else:
                hash_map[s[rightPointer]] = 1


            if hash_map[s[rightPointer]] > largestNum:
                largestNum=hash_map[s[rightPointer]]
                largestLetter=s[rightPointer]

            while ((rightPointer+1)-leftPointer) - largestNum > k:
                hash_map[s[leftPointer]] -= 1
                if largestLetter == s[leftPointer]: largestNum-=1
                for letter, number in hash_map.items():
                    if number > largestNum:
                        largestNum=number
                        largestLetter = letter
                leftPointer+=1

            if rightPointer - leftPointer >= subString: subString = (rightPointer+1 - leftPointer)
            rightPointer+=1

        return subString