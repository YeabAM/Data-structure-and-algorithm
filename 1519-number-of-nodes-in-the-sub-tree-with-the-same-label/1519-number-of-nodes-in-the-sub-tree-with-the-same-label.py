class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        ans = [0 for _ in range(n)]
        
        for e1, e2 in edges:
            tree[e1].append(e2)
            tree[e2].append(e1)
            
        
        def dfs(node,parent):
            total = [0 for _ in range(26)]
            if tree[node] == 0:
                pos = ord(labels[node]) - 97
                total[pos] += 1
                return total
            
            for edge in tree[node]:
                if edge != parent:
                    curr = dfs(edge,node)
                    for i in range(26):
                        total[i] += curr[i]
                        
            pos = ord(labels[node]) - 97
            total[pos] += 1
            ans[node] = total[pos]
            return total
        
        dfs(0,-1)
        return ans
            
                
            
            
            
            
            
        
        
        
            
            
                    