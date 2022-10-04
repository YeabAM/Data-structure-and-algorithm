class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        r,c = 0,0
        
        while len(ans) < n*m:
            i,j = r,c
            visited = set()
            
            for l in range(j, n - c):
                ans.append(matrix[i][l])
                visited.add((i,l))
                j += 1
            
            j -= 1
            i += 1
            
            for k in range(i, m - r):
                ans.append(matrix[k][j])
                visited.add((k,j))
                i += 1
            i -= 1
            j -= 1
            
            for o in range(j, c - 1 ,-1):
                if (i,o) not in visited:
                    ans.append(matrix[i][o])
                j-=1
            j += 1
            i -= 1
            
            for p in range(i, r ,-1):
                if (p,j) not in visited:
                    ans.append(matrix[p][j])
            
            r+=1
            c+=1
            
        return ans