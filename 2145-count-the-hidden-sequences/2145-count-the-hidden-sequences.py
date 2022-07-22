class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        seq = [1] * (len(differences) + 1)
        
        
        for i in range(1,len(differences) + 1):
            seq[i] = seq[i-1] + differences[i-1]
        print(seq)    
        rng = max(seq) - min(seq)
        total = (upper - lower + 1) - rng 
        return total if total > 0 else 0
            
        