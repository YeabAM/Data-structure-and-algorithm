class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        count = 0
        
        for start, dest in connections:
            graph[start].append((dest, True))
            graph[dest].append((start, False))
            
        queue = deque()
        queue.append((-1, 0))
        
        while queue:
            level = len(queue)
            
            for _ in range(level):
                parent, curr = queue.popleft()
                
                for nei, check in graph[curr]:
                    if nei != parent:
                        if check:
                            count += 1
                            
                        queue.append((curr, nei))
                        
        return count