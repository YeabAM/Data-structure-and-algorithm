class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(curRoom):
            visited.add(curRoom)
            
            for key in rooms[curRoom]:
                if key not in visited:
                    dfs(key)
                    visited.add(key)
        
        dfs(0)
        return len(visited) == len(rooms)
        