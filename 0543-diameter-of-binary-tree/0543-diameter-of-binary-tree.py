# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxValue = float('-inf')
        
        def dfs(root):
            nonlocal maxValue
            
            if not root:
                return 0
            
            right = dfs(root.right) 
            left = dfs(root.left) 
            
            maxValue = max(maxValue, right + left)
            
            return max(left, right) + 1
        
        dfs(root)
        
        return maxValue
            
        
        