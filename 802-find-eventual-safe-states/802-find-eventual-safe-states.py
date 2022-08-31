class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        incoming = defaultdict(list)
        outgoing = defaultdict(int)
        safeNodes = []
        for i in range(len(graph)):
            outgoing[i] = len(graph[i])
            
            for j in range(len(graph[i])):
                incoming[graph[i][j]].append(i)
                
        queue = deque([])
        
        for node in outgoing:
            if outgoing[node] == 0:
                queue.append(node)
        
        while queue:
            curr = queue.popleft()
            safeNodes.append(curr)
            for node in incoming[curr]:
                outgoing[node] -= 1
                if outgoing[node] == 0:
                    queue.append(node)
                    
        return sorted(safeNodes)
                    
        