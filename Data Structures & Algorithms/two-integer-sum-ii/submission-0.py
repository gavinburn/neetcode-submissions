class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer=0
        rightPointer=len(numbers)-1
        for i,num in enumerate(numbers):
            sum=numbers[leftPointer] + numbers[rightPointer]
            if sum>target:
                rightPointer-=1
            elif sum<target:
                leftPointer+=1
            else:
                return([leftPointer+1, rightPointer+1])
            sum=0


        return False