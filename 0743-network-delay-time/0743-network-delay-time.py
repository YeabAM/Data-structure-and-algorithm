class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #use heap to access current node
        accessedNodes = []
        heapq.heappush(accessedNodes, (0, k))
        
        TotalTime = 0
        visited = set()
        
        #create a graph based on the edges
        network = defaultdict(list)
        
        for src, dest, cost in times:
            network[src].append([dest, cost])
            
        
        while accessedNodes:
            currCost, currNode = heapq.heappop(accessedNodes)
            #avoiding revisitation of nodes
            if currNode in visited:
                continue
            
            visited.add(currNode)
            TotalTime = max(TotalTime, currCost)
                
            for connectedNode, cost in network[currNode]:
                if connectedNode not in visited:
                    heapq.heappush(accessedNodes, (cost + currCost, connectedNode))
                
        visitedNodes = len(visited)
        
        if visitedNodes == n:
            return TotalTime
        else:
            return -1
            
                
        