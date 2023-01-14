class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        rank = {}
        allStr = set()
        
        for i in range(len(s1)):
            parent[s1[i]] = s1[i]
            parent[s2[i]] = s2[i]
            rank[s1[i]] = 1
            rank[s2[i]] = 1
            allStr.add(s1[i])
            allStr.add(s2[i])
            
            
        def find(letter):
            if parent[letter] == letter:
                return letter
            
            parent[letter] = find(parent[letter])
            
            return parent[letter]
        
        def union(l1, l2):
            p1 = find(l1)
            p2 = find(l2)
            
            if p1 != p2:
                
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                    
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
                    
        
        for l1, l2 in zip(s1, s2):
            # print(l1, l2)
            union(l1, l2)
            
        equiv = []
        smallest = {}
    
        
        for letter in allStr:
            currPrnt = find(letter)
            
            minStr = 'z'
            
            for nei in allStr:
                if find(nei) == currPrnt:
                    minStr = min(minStr, nei)
                    
            smallest[currPrnt] = minStr
            
        for letter in baseStr:
            if letter in allStr:
                curr = find(letter)
                equiv.append(smallest[curr])
            
            else:
                equiv.append(letter)
            
            
        return "".join(equiv)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
                    
        
        