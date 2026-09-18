class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startingIndex = 0
        currentIndex = 0
        currentGas = gas[currentIndex]
        output = -1

        while startingIndex < len(gas):
            nextCost = cost[currentIndex%len(cost)]
            nextGas = gas[(currentIndex+1)%len(gas)]

            if nextCost > currentGas:
                startingIndex = currentIndex + 1
                currentIndex=startingIndex
                currentGas = gas[currentIndex%len(gas)]
            else:
                currentGas -= nextCost
                currentGas += nextGas
                currentIndex = currentIndex + 1
                if currentIndex%len(gas) == startingIndex:
                    output = startingIndex
                    break

        return output