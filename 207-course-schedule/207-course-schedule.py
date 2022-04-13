class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        income = dict()
        preqs = defaultdict(list)
        queue = deque()
        courses = []
        for c in prerequisites:
            income[c[0]] = 0
            income[c[1]] = 0
        
        for cour, pre in prerequisites:
            preqs[pre].append(cour)
            income[cour] += 1
        
        for cour in income:
            if income[cour] == 0:
                queue.append(cour)
        
        while queue:
            curr = queue.popleft()
            courses.append(curr)
            for cour in preqs[curr]:
                income[cour] -= 1
                if income[cour] == 0:
                    queue.append(cour)
                    
        return len(income) == len(courses)
            
        
        