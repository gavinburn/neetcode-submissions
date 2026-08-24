from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)
        visited = set()

        for item in prerequisites:
            course = item[0]
            preReq = item[1]

            if preReq not in preMap[course]:
                preMap[course].append(preReq)


        
        def recurse(course):

            if course in visited:
                return False

            if len(preMap[course]) == 0:
                return True
            
            visited.add(course)
            for preReq in preMap[course]:
                if recurse(preReq) is True:
                    preMap[course].remove(preReq)
                else: return False

            visited.remove(course)
            return True


        
        returnVal = True
        for i in range(numCourses):
            if recurse(i) is not True: returnVal = False

        return returnVal



        

        