class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))

            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            while queue:
                row, col = queue.popleft()

                for rowChange, colChange in directions:
                    newRow = row + rowChange
                    newCol = col + colChange
                    if (
                        0 <= newRow < rows and
                        0 <= newCol < cols and
                        grid[newRow][newCol] == "1" and
                        (newRow, newCol) not in visited
                    ):
                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1

        return islands
        