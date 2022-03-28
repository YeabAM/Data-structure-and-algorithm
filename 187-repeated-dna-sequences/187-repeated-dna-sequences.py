class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = set ()
        repeated = set ()
        
        for i in range(len(s)):
            # print(s[i])
            sequence = s[i:i+10]
            if sequence in visited:
                repeated.add(sequence)
                
            visited.add(sequence)
            
        return list(repeated)
        