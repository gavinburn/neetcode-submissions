class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currentIndex = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.currentIndex >=0:
            if(val<self.minStack[self.currentIndex]):
                self.minStack.append(val)
            else: self.minStack.append(self.minStack[self.currentIndex])
        else: self.minStack.append(val)
        self.currentIndex +=1


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.currentIndex-=1


    def top(self) -> int:
        return(self.stack[self.currentIndex])


    def getMin(self) -> int:
        return self.minStack[self.currentIndex]
