class UnionFind:
    def __init__(self, N):
        self.parent = {i: i for i in range(N)}
        
    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self,u, v):
        root1, root2 = self.find(u), self.find(v)

        if root1 != root2:
            self.parent[root1] = root2
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        prev_occur = defaultdict(int)
        accounts_dict = defaultdict(list)
        ans = []
    
        for i in range(n):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in prev_occur and prev_occur[accounts[i][j]]!=i:
                    uf.union(prev_occur[accounts[i][j]], i)
                prev_occur[accounts[i][j]] = i
        
        for i in range(n):
            accounts_dict[uf.find(i)].append(i)
        
        for k in accounts_dict.keys():
            temp = set()
            for i in accounts_dict[k]:
                for j in range(1, len(accounts[i])):
                    temp.add(accounts[i][j])
            ans.append([accounts[k][0]] + sorted(temp))
        
        return ans
            
            
            
                    
                    
        
        
        