class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += str(len(word))
            encodedString += "#"
            encodedString += word

        return(encodedString)



    def decode(self, s: str) -> List[str]:
        currentPos = 0;
        wordStr = ""
        wordLength=0;
        stringLength = len(s)
        finalRes = [];

        while currentPos < stringLength:
            while s[currentPos] != "#":
                wordStr+= s[currentPos]
                currentPos +=1
            wordLength = int(wordStr)
            finalRes.append(s[currentPos+1 : currentPos+wordLength+1])
            currentPos += wordLength + 1
            wordLength=0
            wordStr = ""

        return(finalRes)