class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        colSets = [set() for _ in range(9)]  # One set for each column
        squareSets = [set() for _ in range(3)]
        rowIndex = 0
        for row in board:
            colIndex = 0
            if(rowIndex%3==0):
                #change so that we clear the individual sets
                squareSets[0].clear()
                squareSets[1].clear()
                squareSets[2].clear()
            for item in row:
                if (item not in rowSet and item not in colSets[colIndex]):
                    if item != ".":
                        rowSet.add(item)
                        colSets[colIndex].add(item)
                else: return False
                squareSetIndex = colIndex//3
                if item not in squareSets[squareSetIndex]:
                    if item != ".":
                        squareSets[squareSetIndex].add(item)
                else : return False

                colIndex+=1
            rowIndex+=1
            rowSet.clear()

        return True