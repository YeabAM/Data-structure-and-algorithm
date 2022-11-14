class Solution:
    def find(self, stone, parents):
        if parents[stone] == stone:
            return stone
        parents[stone] = self.find(parents[stone], parents)
        
        return parents[stone]
    
    def union(self,stone1, stone2, parents):
        p1 = self.find(stone1, parents)
        p2 = self.find(stone2, parents)
        
        if p1 != p2:
            parents[p1] = p2
            
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = {}
        
        for x, y in stones:
            cell = (x, y)
            parents[cell] = cell
            
        for i, stone1 in enumerate(stones):
            for j, stone2 in enumerate(stones):
                if i != j:
                    if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                        cell = (stone1[0], stone1[1])
                        cell2 = (stone2[0], stone2[1])
                        
                        self.union(cell, cell2, parents)
                        
        components = 0
        for parent in parents:
            if parents[parent] == parent:
                components += 1
        
        return len(stones) - components
            
                    
            
        
        
    
            
        
    
            
        
        