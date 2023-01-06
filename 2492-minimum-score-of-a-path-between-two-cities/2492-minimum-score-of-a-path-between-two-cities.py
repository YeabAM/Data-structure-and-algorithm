class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        min_score = float('inf')
        
        graph = defaultdict(list)
        edge_count = defaultdict(int)
        
        for city1, city2, cost in roads:
            graph[city1].append((city2, cost))
            graph[city2].append((city1, cost))
            edge_count[city1] += 1
            edge_count[city2] += 1
        
        queue = deque()
        queue.append((-1, 1))
        # print(edge_count,'b')
        while queue:
            level = len(queue)
            
            for _ in range(level):
                init, curr = queue.popleft()
                # print(init, curr)
                for city, cost in graph[curr]:
                    if city != init:
                        edge_count[curr] -= 1
                        edge_count[city] -= 1
                        if edge_count[city] > 0:
                            queue.append((curr, city))
                            
                        min_score = min(cost, min_score)
                            
                        # print(edge_count, city)
                    
        return min_score
                        
        
        
        