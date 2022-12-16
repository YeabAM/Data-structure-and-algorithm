class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        indicies = defaultdict(set)
        for i in range(len(arr)):
            indicies[arr[i]].add(i)
        queue = deque()
        visited = set()
        queue.append(0)
        visited.add(0)
        level = 0
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == len(arr) - 1:
                    return level

                while indicies[arr[curr]]:
                    idx = indicies[arr[curr]].pop()
                    if idx not in visited:
                        if idx == len(arr) - 1:
                            return level + 1
                        
                        queue.append(idx)
                        visited.add(idx)
                        
                left = curr - 1 
                right = curr + 1

                if left not in visited and left >= 0:
                    if left == len(arr) - 1:
                        return level + 1
                    
                    queue.append(left)
                    visited.add(left)

                if right not in visited and right < len(arr):
                    if right == len(arr) - 1:
                        return level + 1

                    queue.append(right)
                    visited.add(right)

            level += 1