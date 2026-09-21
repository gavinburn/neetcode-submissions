from collections import deque
from collections import defaultdict
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        steps = defaultdict(int)
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1: return -1
        queue.append((0,0))
        visited.add((0,0))
        steps[(0,0)] = 1

        directions = {
            (0,-1),
            (0,1),
            (-1, 0),
            (1, 0),
            (1,1),
            (1,-1),
            (-1,1),
            (-1,-1)
        }

        while queue:
            location = queue.popleft()
            updatedLocation = (0,0)

            if steps[(rows-1, cols-1)] > 0: break

            for direction in directions:
                updatedLocation = (location[0] + direction[0], location[1] + direction[1])

                if updatedLocation in visited: continue
                if updatedLocation[0] < 0 or updatedLocation[0] >= rows: continue
                if updatedLocation[1] < 0 or updatedLocation[1] >= cols: continue

                if grid[updatedLocation[0]][updatedLocation[1]] == 0:
                    queue.append(updatedLocation)
                    if steps[updatedLocation] == 0: steps[updatedLocation] = steps[location]+1

                visited.add(updatedLocation)

        if steps[(rows-1, cols-1)] > 0: return steps[(rows-1, cols-1)]
        else: return -1


        