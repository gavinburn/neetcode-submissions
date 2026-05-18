class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque();
        for bracket in s:
            if bracket in ("(" , "{" , "["):
                stack.append(bracket)
            elif bracket in (")" , "}" , "]"):
                if(len(stack)!=0):
                    top = stack.pop()
                    if (bracket==")"):
                        if top!="(": return False
                    if(bracket == "}"):
                        if top != "{": return False
                    if (bracket == "]"):
                        if top != "[": return False
                else: return False

        if(len(stack)!=0): return False
        else: return True