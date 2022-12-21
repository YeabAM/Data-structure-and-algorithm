class Solution:
             
    def canCross(self, stones: List[int]) -> bool:
        
        pos = defaultdict(lambda : -1)
        
        for idx, val in enumerate(stones):
            pos[val] = idx
            
        moves = (-1, 0, 1)
        
        @lru_cache(None)
        def is_possible(idx, steps):
            
            if idx == len(stones) - 1:
                return True
            
            for move in moves:
                next_stone = pos[stones[idx] + steps + move]
                # print(idx, steps, next_stone, stones[idx] + steps + move)
                if next_stone != -1 and next_stone > idx:
                    
                    if is_possible(next_stone, steps + move):
                        return True
            return False
            
                
        return is_possible(0, 0)
    
    
        
        
    
        
        