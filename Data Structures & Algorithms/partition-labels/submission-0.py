from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastIndex = defaultdict(int)
        output = []

        for i in range(len(s)):

            lastIndex[s[i]] = i


        substringMax = lastIndex[s[0]]
        prevIndex=-1
        for i in range(len(s)):
            
            if lastIndex[s[i]] > substringMax: 
                substringMax = lastIndex[s[i]]
            
            
            if i == substringMax: 
                output.append(i-prevIndex)
                prevIndex = substringMax
                
            





        return output