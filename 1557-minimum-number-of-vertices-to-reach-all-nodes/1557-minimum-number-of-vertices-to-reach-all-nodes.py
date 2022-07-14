class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        outgoing = set([i for i in range(n)])
        print(outgoing)
        
        for fr, to in edges:
            if to in outgoing:
                outgoing.remove(to)
        outgoing = list(outgoing)
        
        return outgoing
            
            
            
        