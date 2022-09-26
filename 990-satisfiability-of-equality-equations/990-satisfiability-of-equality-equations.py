class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [-1 for _ in range(26)]
        eq = []
        ineq = []
        for equation in equations:
            if equation[1] != "!":
                eq.append((equation[0], equation[3]))
            else:
                ineq.append((equation[0], equation[3]))
            

        def union(node1, node2):
                root1, root2 = find(node1), find(node2)
                if root1 != root2:
                    parent[root1] = root2

        def find(node):
            if parent[node] == -1:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        for u, v in eq:
            union(ord(u) - 97,ord(v) - 97)
            
        for u, v in ineq:
            if find(ord(u) - 97) == find(ord(v) - 97):
                return False
        
        return True
        

        