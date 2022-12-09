# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, path):
            if not node:
                return "|"
            
            if not node.right and not node.left:
                curr = path + chr(97 + node.val)
                return curr[::-1]
            
            curr = chr(97 + node.val)
            
            right = dfs(node.right, path + curr)
            left = dfs(node.left, path + curr)
                
            return min(right, left)
        
        
        return dfs(root, "")
                
            
                
        