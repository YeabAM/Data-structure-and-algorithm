class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        neigh = defaultdict(set)
        queue = deque()
        courses = []
        
        for i in range(numCourses):
            indegree[i] = 0
        
        for dest, src in prerequisites:
            neigh[src].add(dest)
            indegree[dest] += 1
            
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            curr = queue.popleft()
            courses.append(curr)
            
            for des in neigh[curr]:
                indegree[des] -= 1
                if indegree[des] == 0:
                    queue.append(des)
                    
        return len(courses) == numCourses
                
                
            
        
        