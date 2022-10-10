# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxx = 0
        
        
        def dfs(node, rootVal):
            nonlocal maxx
            if not node:
                return 0
            
            left = dfs(node.left, node.val)    
            right = dfs(node.right, node.val)
            maxx = max(maxx, left + right)
            
            if node.val == rootVal:
                return max(left, right) + 1
                
            else:
                return 0
                
        dfs(root,float('inf'))   
        return maxx
                
        