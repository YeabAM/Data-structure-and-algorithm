class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        ans = 1
        
        for node, parent in enumerate(parent):
            graph[parent].append(node)
            
        
        def dfs(node):
            nonlocal ans
            longest = secondLongest = 0
            
            for child in graph[node]:
                currPath = dfs(child)
            
                if s[child] != s[node]:
                    
                    if currPath > longest:
                        secondLongest = longest
                        longest = currPath
                        
                    elif currPath > secondLongest:
                        secondLongest = currPath
                    
            ans = max(ans, longest + secondLongest + 1)
                    
            return longest + 1
            
        dfs(0)
        
        return ans
            
        