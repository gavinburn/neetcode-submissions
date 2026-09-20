from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0: 
            return False

        iterations = len(hand) // groupSize

        freqCount = defaultdict(int)

        for card in hand:
            freqCount[card] +=1
            


        sortedMap = dict(sorted(freqCount.items()))
        sortedKeys = sorted(freqCount.keys())

        print(sortedMap)
        print(sortedKeys)


        for i in range(iterations):

            lastItem = None

            for key in sortedKeys:
                if sortedMap[key] > 0:
                    minKey = key
                    break
            for k in range(groupSize):
                if lastItem is None:
                    lastItem = minKey
                    sortedMap[minKey] -=1
                else: 
                    if lastItem+1 in sortedMap and sortedMap[lastItem+1]>0:
                        lastItem = lastItem+1
                        sortedMap[lastItem] -=1
                    else:
                        return False

        return True

        