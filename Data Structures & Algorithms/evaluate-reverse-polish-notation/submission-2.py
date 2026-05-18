class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for number in tokens:
            if(number not in ["+", "-", "*", "/"]):
                stack.append(number)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if(number=="+"):
                    res = num1 + num2
                elif(number=="-"):
                    res = num2 - num1
                elif (number == "*"):
                    res = num1 * num2
                elif (number == "/"):
                    res = int(num2 / num1)
                stack.append(str(res))
        return int(stack.pop())