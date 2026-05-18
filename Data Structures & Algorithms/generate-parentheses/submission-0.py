class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(leftBracket, rightBracket):

            if leftBracket == rightBracket == n:
                res.append("".join(stack))
                return
            if leftBracket < n:
                stack.append("(")
                backtrack(leftBracket+1, rightBracket)
                stack.pop()
            if rightBracket < leftBracket:
                stack.append(")")
                backtrack(leftBracket, rightBracket+1)
                stack.pop()


        backtrack(0, 0)
        return res