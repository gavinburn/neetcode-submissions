class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        numRows = len(heights)
        numCols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row, column, prev, ocean):
                
            if ocean == "Atlantic":
                if (row, column) in atlantic: return
            else:
                if (row, column) in pacific: return
                

            if row < 0 or column < 0 or row >=numRows or column >=numCols or heights[row][column] < prev:
                return

            if ocean == "Atlantic":
                atlantic.add((row, column))
            else:
                pacific.add((row, column))

            dfs(row+1, column, heights[row][column], ocean)
            dfs(row-1, column, heights[row][column], ocean)
            dfs(row, column+1, heights[row][column], ocean)
            dfs(row, column-1, heights[row][column], ocean)

        for col in range(numCols):
            dfs(0, col, 0, "Pacific")
            

        for row in range(numRows):
            dfs(row, 0, 0, "Pacific")


        for col in range(numCols):
            dfs(numRows-1, col, 0, "Atlantic")

               
        for row in range(numRows):
            dfs(row, numCols-1, 0, "Atlantic")

        output = sorted(pacific & atlantic)

        outputList = []

        for cell in output:
            outputList.append(list(cell))

        return outputList
        