class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        upper_bound = max(forbidden) + a + b + x
        # upper_bound = max(max(forbidden) , x) + a + b
        forbidden = set(forbidden)
        queue = deque()
        queue.append((0, 0, 1))
        visited = set((0, 1))
        
        
        while queue:
            pos, steps, back = queue.popleft()
            # print(pos)
            
            if pos == x:
                return steps
            
            if pos + a < upper_bound and (pos + a, 0) not in visited and (pos + a) not in forbidden:
                visited.add((pos + a, 0))
                queue.append((pos + a, steps + 1, 0))
            
            if pos - b > 0 and back == 0 and (pos - b, 1) not in visited and (pos - b) not in forbidden:
                visited.add((pos - b, 1))
                queue.append((pos - b, steps + 1, 1))
                
            
                
                
        return -1
                
            
            
        