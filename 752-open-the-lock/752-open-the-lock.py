class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        deadends = set(deadends)
        level = 0
        queue.append('0000')
        
        if '0000' in deadends:
            return -1
        
        while queue:
            l = len(queue)
            
            for _ in range(l):
                curr = queue.popleft()
                if curr == target: return level
                for i in range(4):
                    num = int(curr[i:i+1])
                    up = num  + 1 if num < 9 else 0
                    down = num - 1 if num > 0 else 9
                    
                    newComb = curr[:i] + str(up) + curr[i+1:]
                    
                    if newComb not in deadends:
                        queue.append(newComb)
                        deadends.add(newComb)
                        
                    newComb = curr[:i] + str(down) + curr[i+1:]
                    
                    if newComb not in deadends:
                        queue.append(newComb)
                        deadends.add(newComb)
                        
            level += 1
            
        return -1
                        
                    
            
                
        