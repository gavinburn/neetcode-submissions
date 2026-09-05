import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        returnDistances = []
        distanceMap = defaultdict(list)
        heapq.heapify(distances)


        for point in points:
            arg1 = point[0] * point[0]
            arg2 = point[1] * point[1]
            distance = math.sqrt(arg1 + arg2)
            heapq.heappush(distances, distance)
            distanceMap[distance].append(point)
        

        for i in range(k):
            top = heapq.heappop(distances)
            coOrd = distanceMap[top][-1]
            distanceMap[top].pop()
            returnDistances.append(coOrd)

        return returnDistances
