class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        incoming = defaultdict(list)
        outgoing = defaultdict(int)
        queue = deque()
        ans = []
        
        for i in range(len(graph)):
            outgoing[i] = len(graph[i])
            for j in graph[i]:
                incoming[j].append(i)
        
        for i in range(len(graph)):
            if outgoing[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            
            for n in incoming[cur]:
                outgoing[n] -= 1
                if outgoing[n] == 0:
                    queue.append(n)
                
        return sorted(ans)
                    