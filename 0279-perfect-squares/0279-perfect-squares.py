class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque()
        queue.append(n)
        visited = set()
        count = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                num = queue.popleft()
                
                temp = floor(sqrt(num))
                for val in range(1, temp+1):
                    toAdd = num - val ** 2
                    if toAdd not in visited:
                        if toAdd == 0:
                            return count
                        
                        queue.append(toAdd)
                        visited.add(num)
                    
            count += 1