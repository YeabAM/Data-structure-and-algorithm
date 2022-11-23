class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        longest_path = 1
        n = len(parent)
        # convert list to graph
        graph = defaultdict(list)
        for index in range(1,n):
            graph[parent[index]].append(index)

        def dfs(currNode):
            nonlocal longest_path
            if not graph[currNode]:return 1
            currLongestPath = 1
            for child in graph[currNode]:
                childLongestPath = dfs(child)
                if s[currNode] != s[child]:
                    longest_path = max(longest_path,childLongestPath+currLongestPath)
                    currLongestPath = max(currLongestPath,childLongestPath+1)
            return currLongestPath
        dfs(0)
        return longest_path
            
        