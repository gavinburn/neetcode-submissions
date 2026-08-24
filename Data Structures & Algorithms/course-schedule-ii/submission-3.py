class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        visited = set()
        completed = set()
        output = []

        for item in prerequisites:
            course = item[0]
            preReq = item[1]

            if preReq not in preMap[course]:
                preMap[course].append(preReq)


        
        def recurse(course):

            if course in visited:
                return False

            if len(preMap[course]) == 0:
                if course not in completed:
                    output.append(course)
                    completed.add(course)
                return True
            
            visited.add(course)
            for preReq in preMap[course]:
                if recurse(preReq) is False: return False

            visited.remove(course)
            preMap[course] = []
            if course not in completed:
                output.append(course)
                completed.add(course)
            return True


        
        returnVal = True
        append = True
        for i in range(numCourses):
            if recurse(i) is not True: returnVal = False
        
        if returnVal: return output
        else: return []


        

        