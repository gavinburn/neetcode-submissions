class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.curr = ""
        self.rows = len(board)
        self.columns = len(board[0])
        self.flag = False

        def check(row, column, wordsAdded):
            if self.flag:
                return

            if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
                return

            if board[row][column] != word[wordsAdded]:
                return

            self.curr += board[row][column]

            if self.curr == word:
                self.flag = True
                return

            temp = board[row][column]
            board[row][column] = "#"

            check(row + 1, column, wordsAdded + 1)
            check(row - 1, column, wordsAdded + 1)
            check(row, column + 1, wordsAdded + 1)
            check(row, column - 1, wordsAdded + 1)

            board[row][column] = temp
            self.curr = self.curr[:-1]         
            


        for row, lists in enumerate(board):
            for column, item in enumerate(lists):
                if item == word[0]:
                    check(row, column, 0)
        return self.flag



        