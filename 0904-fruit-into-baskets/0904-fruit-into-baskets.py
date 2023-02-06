class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = {}
        max_fruits = 0
        l = 0
        
        for r in range(len(fruits)):
            if fruits[r] in counts:
                counts[fruits[r]] += 1
                
            else:
                counts[fruits[r]] = 1
                
            while len(counts) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                
                l += 1
                
            max_fruits = max(max_fruits, r - l + 1)
        
        
        return max_fruits
        