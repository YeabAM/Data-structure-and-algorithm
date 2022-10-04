class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        amountOfPreq = defaultdict(int)
        PreqFor = defaultdict(set)
        courses = []
        queue = deque()
        
        
        for i in range(numCourses):
            amountOfPreq[i] = 0
            
        for course, preqCourse in prerequisites:
            PreqFor[preqCourse].add(course)
            amountOfPreq[course] += 1
            
        for i in range(numCourses):
            if amountOfPreq[i] == 0:
                queue.append(i)
                
        while queue:
            currCourse = queue.popleft()
            courses.append(currCourse)
            
            for course in PreqFor[currCourse]:
                amountOfPreq[course] -= 1
                if amountOfPreq[course] == 0:
                    queue.append(course)
                    
        return courses if len(courses) == numCourses else []
                
            
        
            
        
        
        