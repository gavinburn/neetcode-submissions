class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        def computeMax(startingTriplet, triple):
            if triple[0] > startingTriplet[0]: startingTriplet[0] = triple[0]
            if triple[1] > startingTriplet[1]: startingTriplet[1] = triple[1]
            if triple[2] > startingTriplet[2]: startingTriplet[2] = triple[2]

        startingTriplet = []


        for triple in triplets:

            if startingTriplet == []:
                if triple[0] <= target[0] and triple[1] <= target[1] and triple[2] <= target[2]:
                    startingTriplet = triple

            else:
                if triple[0] <= target[0] and triple[1] <= target[1] and triple[2] <= target[2]:
                    computeMax(startingTriplet, triple)

            if startingTriplet == target:
                return True
        

        return False

