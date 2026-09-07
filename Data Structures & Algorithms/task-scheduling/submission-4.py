from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []

        def createHeap():
            letterCount = defaultdict(int)

            for letter in tasks:
                letterCount[letter] +=1


            for key,value in letterCount.items():
                maxHeap.append((value,key))

            heapq.heapify_max(maxHeap)
        
        createHeap()
        print(maxHeap)
        k=0
        waiting=0
        holdingQueue = []
        while len(maxHeap) > 0 or waiting > 0:
            if len(maxHeap) > 0:
                top = heapq.heappop_max(maxHeap)
                if top[0]-1>0:
                    newTop = (top[0]-1, top[1])
                    holdingQueue.append(newTop)
                    waiting +=1
                else:
                    holdingQueue.append(None)
            else:
                holdingQueue.append(None)
            if k-n >= 0:
                if holdingQueue[k-n] is not None:
                    heapq.heappush_max(maxHeap, holdingQueue[k-n])
                    holdingQueue[k - n] = None
                    waiting -=1
            k+=1

        return k


        