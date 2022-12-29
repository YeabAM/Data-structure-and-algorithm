class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        heapq.heapify(tasks)
        time = tasks[0][0]
        curr_tasks = []
        order = []
        
        while tasks or curr_tasks:
            while tasks and tasks[0][0] <= time:
                start, t, idx = heapq.heappop(tasks)
                heapq.heappush(curr_tasks, (t, idx))
                
            if curr_tasks:
                processed = heapq.heappop(curr_tasks)
                order.append(processed[1])
                time += processed[0]
            
            elif tasks:
                time = tasks[0][0]
                
        
        return order
        