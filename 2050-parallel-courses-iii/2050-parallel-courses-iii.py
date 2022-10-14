class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        incoming = {}
        totalTime = 0
        for i in range(1, n+1):
            incoming[i] = [0,0]
            
        for prev, cour in relations:
            graph[prev].append(cour)
            incoming[cour][0] += 1
            
        queue = deque()
            
        for i in range(1, n+1):
            if incoming[i][0] == 0:
                queue.append([i,incoming[i]])
                
        while queue:
            cour, maxtime = queue.popleft()
            # print(cour, "head",incoming[cour])
            totalTime = max(totalTime, maxtime[1] + time[cour - 1])
            for course in graph[cour]:
                # print("before", course, incoming[course][1],cour)
                incoming[course][1] = max(incoming[course][1], incoming[cour][1] + time[cour - 1])
                # print(course, incoming[course][1],cour)
                incoming[course][0] -= 1
                
                if incoming[course][0] == 0:
                    queue.append([course, incoming[course]])
                
        return totalTime
        
            
        