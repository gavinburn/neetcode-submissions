import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            if first == second:
                continue
            elif first > second:
                first = first - second
                heapq.heappush_max(stones, first)

            
        if len(stones) > 0: return stones[0]
        else: return 0