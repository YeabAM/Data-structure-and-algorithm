class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # quitness = quiet[:]
        graph = [[] for _ in range(len(quiet))]
        indegree =[0] * len(quiet) 
        for x, y in richer:
            graph[x].append(y)
            indegree[y] += 1
            
        queue = deque()
        
        for i,g in enumerate(graph):
            if indegree[i] == 0:
                queue.append(i)
                
        ans = [[i,quiet[i]] for i in range(len(quiet))]
        while queue:
            curr = queue.popleft()
            for ne in graph[curr]:
                if ans[ne][1] >= ans[curr][1] :
                    ans[ne] = [ans[curr][0],ans[curr][1]]
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    queue.append(ne)
            # print(ans,curr)
                    
                    
            
        return [p for p,q in ans]
        