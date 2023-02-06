class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque()
        queue.append((0, 0, 1))
        
        while queue:
            length = len(queue)
            
            for _ in range(length):
                steps, pos, speed = queue.popleft()
                if pos == target:
                    return steps
                queue.append((steps + 1, pos + speed, speed * 2))
                
                if (pos+speed) < target and speed < 0 or (pos+speed) > target and speed > 0:
                    speed = 1 if speed < 0 else -1
                    queue.append((steps + 1, pos, speed))
                    
        
            
        