class Solution:
    
    def backtrack(self, idx, quantity, freqs):
        if idx >= len(quantity):
            return True

        for i in range(len(freqs)):
            if freqs[i] >= quantity[idx]:
                # print(i)
                freqs[i] -= quantity[idx]
                
                if self.backtrack(idx+1, quantity, freqs):
    
                    return True

                freqs[i] += quantity[idx]
                
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        intQuantity = defaultdict(int)
        
        for i in nums:
            intQuantity[i] += 1
        
        freqs = sorted(intQuantity.values(), reverse= True)
        quantity.sort(reverse = True)
               
        return self.backtrack(0, quantity, freqs)
            
            
        
            
        
        