# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ancestor = None
        max_level = 0
        
        def dfs(node, level):
            nonlocal ancestor
            nonlocal max_level
            
            if not node:
                return 0
            
            if not node.left and not node.right:
                if level >= max_level:
                    ancestor = node
                    max_level = level
                return 1
            
            left = dfs(node.left, level + 1) 
                
            right = dfs(node.right, level + 1) 
            
            if left == right and level + left >= max_level:
                ancestor = node
                max_level = level + left
            
            return max(left, right) + 1
        
        dfs(root, 1)
        return ancestor