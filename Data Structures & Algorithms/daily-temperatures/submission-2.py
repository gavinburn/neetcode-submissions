class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        numDays = 0
        numDaysArr=[]
        wasGreater = False
        for i in range(len(temperatures)):
            stack.append(temperatures[i])
            k=i+1
            while(k<len(temperatures)):
                if temperatures[k] > stack[-1]:
                    stack.pop()
                    if(len(stack)==0):
                        numDays += 1
                        wasGreater=True
                        break
                else:
                    stack.append(temperatures[k])
                    numDays+=1
                    k+=1
            if wasGreater==False:numDays=0
            numDaysArr.append(numDays)
            numDays=0
            wasGreater=False
            stack.clear()
        return numDaysArr