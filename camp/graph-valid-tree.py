
from collections import defaultdict
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        visited = set()
        nodes = defaultdict(list)
        for start,end in edges:
            nodes[start].append(end)
            nodes[end].append(start)


        # write your code here
        def dfs (node, parent):
            print("node=", node, "parent=", parent)
            print("ch", nodes[node])
            # if node in visited and node != parent:
            #     return False
            
            for nd in nodes[node]:
                print("nd", nd)
                if nd in visited and nd != parent:
                    return False
                elif nd not in visited:
                    visited.add(nd)    
                    dfs(nd, node)
                    
                    
        
        visited.add(0)           
        result = dfs(0,-1)
        
        print(visited)
        print(nodes)
        print(result,n, len(visited))
        if len(visited) == n and result == None:
            return True
        return False 

            
        