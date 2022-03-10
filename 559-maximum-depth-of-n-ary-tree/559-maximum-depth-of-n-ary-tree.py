
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if not root:
                return 0
            dp = 1
            for child in root.children:
                dp = max(dp,1 + dfs(child))
            return dp                        
        return dfs(root)




