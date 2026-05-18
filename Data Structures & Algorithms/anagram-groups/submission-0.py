class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainDict = defaultdict(list)

        for word in strs:
            letterArr = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                letterArr[index] +=1

            key = tuple(letterArr)
            mainDict[key].append(word)


        return(list(mainDict.values()))